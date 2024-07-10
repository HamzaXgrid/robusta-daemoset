from hikaru.model.rel_1_26 import DaemonSet
from robusta.api import (
    DaemonSetEvent,
    action, PodEvent

)

@action
def daemonset_status_enricher(event: DaemonSetEvent):
    """
    Enrich the finding with daemon set stats.

    Includes recommendations for the identified cause.
    """
    print("---------------------------- Daemon Set -------------------------------------")
    DaemonSet = event.get_daemonset()
    #print("daemonset is ",DaemonSet)
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
    
    # # Check if tolerations already exist and add if they do not
    existing_tolerations = DaemonSet.spec.template.spec.tolerations or []
    for new_toleration in new_tolerations:
        if new_toleration not in existing_tolerations:
            existing_tolerations.append(new_toleration)
    print(existing_tolerations)
    print("Tolerations Added")
    DaemonSet.spec.template.spec.tolerations = existing_tolerations
    
    # Update the DaemonSet with the new tolerations
    DaemonSet.update()

