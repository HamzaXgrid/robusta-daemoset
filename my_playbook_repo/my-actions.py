from hikaru.model.rel_1_26 import DaemonSet, NodeList, Toleration
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
    print("---------------------------- Daemon Set -------------------------------------")
    DaemonSet = event.get_daemonset()

    # Load Kubernetes config
    # config.load_incluster_config()
    # v1 = client.CoreV1Api()
    
    # Get all nodes
    nodes = NodeList.readNamespacedNodeList()
    print(nodes)
    # Extract taints from nodes
    new_tolerations = []

    for node in nodes.items:
        if node.spec.taints:
            for taint in node.spec.taints:
                new_tolerations.append(
                    Toleration(
                        key=taint.key,
                        operator="Equal" if taint.value else "Exists",
                        value=taint.value,
                        effect=taint.effect,
                        tolerationSeconds=taint.tolerationSeconds
                    )
                )
    print("-----------------------------------")
    print(new_tolerations)
    # # Check if tolerations already exist and add if they do not
    # existing_tolerations = DaemonSet.spec.template.spec.tolerations or []
    # for new_toleration in new_tolerations:
    #     if new_toleration not in existing_tolerations:
    #         existing_tolerations.append(new_toleration)
    # print(existing_tolerations)
    # print("Tolerations Added")
    # DaemonSet.spec.template.spec.tolerations = existing_tolerations
    
    # # Update the DaemonSet with the new tolerations
    # DaemonSet.update()

