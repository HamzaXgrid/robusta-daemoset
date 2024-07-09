from hikaru.model.rel_1_26 import DaemonSet
from robusta.api import (
    DaemonSetEvent,
    action,
    does_daemonset_have_toleration,
)

@action
def daemonset_status_enricher(event: DaemonSetEvent):
    """
    Enrich the finding with daemon set stats.

    Includes recommendations for the identified cause.
    """
    DaemonSet = event.get_daemonset()
    
    # Define the tolerations to be added
    new_tolerations = [
        {
            "key": "key1",
            "operator": "Equal",
            "value": "value1",
            "effect": "NoSchedule"
        },
        {
            "key": "key2",
            "operator": "Exists",
            "effect": "NoExecute",
            "tolerationSeconds": 3600
        }
    ]
    
    # Check if tolerations already exist and add if they do not
    existing_tolerations = DaemonSet.spec.template.spec.tolerations or []
    for new_toleration in new_tolerations:
        if new_toleration not in existing_tolerations:
            existing_tolerations.append(new_toleration)
    
    DaemonSet.spec.template.spec.tolerations = existing_tolerations
    
    # Update the DaemonSet with the new tolerations
    DaemonSet.update()

@action
def delete_pod(event: PodEvent):
    """
    Deletes a pod
    """
    if not event.get_pod():
        raise ActionException(ErrorCodes.RESOURCE_NOT_FOUND, "Failed to get the pod for deletion")

    event.get_pod().delete()