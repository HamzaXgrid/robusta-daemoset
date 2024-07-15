from robusta.api import  PersistentVolumeEvent, action
from kubernetes import client, config

from hikaru.model.rel_1_26 import (
    PersistentVolumeClaim,
    PersistentVolumeClaimVolumeSource,

)

@action
def resize_pv(event: PersistentVolumeEvent):
    config.load_incluster_config()
    pv = event.get_persistentvolume()
    pv_claimref = pv.spec.claimRef
    print(pv)
    print("------------------")
    print(pv_claimref)
    # persistentVolume = event.get_persistentvolume()
    # api = client.CoreV1Api()
    # persistentVolumeName = persistentVolume.metadata.name
    # persistentVolumeDetails = api.read_persistent_volume(persistentVolumeName)
    # print("PV is: ", persistentVolumeDetails)
    # if persistentVolumeDetails.spec.claim_ref is not None:# We are checking whether PV is claimed by any PVC.
    #     pvcName = persistentVolumeDetails.spec.claim_ref.name
    #     print("####################################################################")
    #     print(pvcName)
    #     pvcNameSpace = persistentVolumeDetails.spec.claim_ref.namespace
    # else:
    #     print("#############################7######################################")
    #     print(persistentVolumeDetails.spec.claim_ref.name)


    # if not pvc_name or not namespace:
    #     event.add_enrichment([{
    #         "type": "markdown",
    #         "content": f"PVC name or namespace not found in the event."
    #     }])
    #     return

    # # Get the PVC
    # pvc = v1.read_namespaced_persistent_volume_claim(name=pvc_name, namespace=namespace)

    # # Update the PVC size
    # pvc.spec.resources.requests['storage'] = params.new_size

    # # Patch the PVC
    # v1.patch_namespaced_persistent_volume_claim(name=pvc_name, namespace=namespace, body=pvc)

    # # Get the corresponding PV
    # pv_name = pvc.spec.volume_name
    # pv = v1.read_persistent_volume(name=pv_name)

    # # Update the PV size
    # pv.spec.capacity['storage'] = params.new_size

    # # Patch the PV
    # v1.patch_persistent_volume(name=pv_name, body=pv)

    # event.add_enrichment([{
    #     "type": "markdown",
    #     "content": f"Resized PVC `{pvc_name}` in namespace `{namespace}` to `{params.new_size}`"
    # }])

# from hikaru.model.rel_1_26 import Toleration
# from robusta.api import (
#     DaemonSetEvent,
#     action
# )
# from kubernetes import client, config

# @action
# def daemonset_status_enricher(event: DaemonSetEvent):
#     """
#     Enrich the finding with daemon set stats.

#     Includes recommendations for the identified cause.
#     """
#     daemonSet = event.get_daemonset()

#     # Load Kubernetes config
#     config.load_incluster_config()
#     v1 = client.CoreV1Api()
    
#     # Get all nodes
#     nodes = v1.list_node()

#     # Extract taints from nodes
#     newTolerations = []

#     for node in nodes.items:
#         labels = node.metadata.labels
#         if "node-role.kubernetes.io/master" not in labels:
#             if node.spec.taints:
#                 for taint in node.spec.taints:
#                     newTolerations.append(
#                         Toleration(
#                             key=taint.key,
#                             operator="Equal" if taint.value else "Exists",
#                             value=taint.value,
#                             effect=taint.effect,
#                         )
#                     )

#     # # Check if tolerations already exist and add if they do not
#     existingTolerations = daemonSet.spec.template.spec.tolerations or []
#     for newToleration in newTolerations:
#         if newToleration not in existingTolerations:
#             existingTolerations.append(newToleration)
#     daemonSet.spec.template.spec.tolerations = existingTolerations
    
#     # Update the DaemonSet with the new tolerations
#     daemonSet.update()


