from hikaru.model.rel_1_26 import Toleration
from robusta.api import (
    DaemonSetEvent,
    action
)
from kubernetes import client, config

@action
def daemonset_status_enricher(event: DaemonSetEvent):
    """
    Enrich the finding with daemon set stats.

    Includes recommendations for the identified cause.
    """
    daemonSet = event.get_daemonset()

    # Load Kubernetes config
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    
    # Get all nodes
    nodes = v1.list_node()

    # Extract taints from nodes
    newTolerations = []

    for node in nodes.items:
        labels = node.metadata.labels
        if "node-role.kubernetes.io/master" not in labels:
            if node.spec.taints:
                for taint in node.spec.taints:
                    newTolerations.append(
                        Toleration(
                            key=taint.key,
                            operator="Equal" if taint.value else "Exists",
                            value=taint.value,
                            effect=taint.effect,
                        )
                    )
    print("-----------------------------------")
    print(newTolerations)
    # # Check if tolerations already exist and add if they do not
    existingTolerations = daemonSet.spec.template.spec.tolerations or []
    for new_toleration in newTolerations:
        if new_toleration not in existingTolerations:
            print("Existing tolerations are : ",existingTolerations)
            print("New tolerations are : ",new_toleration)
            existingTolerations.append(new_toleration)
    print("Tolerations Added")
    daemonSet.spec.template.spec.tolerations = existingTolerations
    
    # Update the DaemonSet with the new tolerations
    daemonSet.update()

