# gluster-ansible-repositories
Collection of Ansible roles for repository management

Requirements
------------

Ansible version 2.5 or above

Role Variables
--------------

| Name                     |Choices| Default value         | Comments                          |
|--------------------------|-------|-----------------------|-----------------------------------|
| gluster_repos_activationkey |    | UNDEF   | Activation key for enabling the repositories |
| gluster_repos_attach | yes/no   | no    | Whether to auto-attach the available repositories |
| gluster_repos_username  |  | UNDEF | Username for the subscription-manager command |
| gluster_repos_password  |  | UNDEF   | Password for the subscription-manager command |
| gluster_repos_force | yes/no   | no | If set to yes, subscription-manager registers by force even if already registerd |
| gluster_repos_pools  |  | UNDEF | List of pool ids to attach |
| gluster_repos_disable_all  | yes/no | yes | Disable all the repositories before attaching to new repositories |
| gluster_repos_rhsmrepos  | | UNDEF | List of repositories to enable |
| gluster_repos_hci_subscribe | | UNDEF | Attach to HCI repositories |
| gluster_repos_nfsganesha_subscribe  | | UNDEF | Attach to list of NFS Ganesha repositories |
| gluster_repos_smb_subscribe  | | UNDEF | Attach to list of SMB repositores |

Tags
----

| Name             | Comments                                  |
|------------------|-------------------------------------------|
| activationkey | Subscribe to RHSM using activation key |
| register | Register to RHSM using username and password |
| attachpools | Attach the pools to RHSM |
| disablerepos | Disable all the repos |
| enablerepos | Enable the given set of repositories |
| hcisubscribe | Enable the repositories required for HCI |
| nfsganeshasubscribe | Enable the repositories required for NFS Ganesha  |
| smbsubscribe | Enable the repositories required for Samba |

Example Playbook
----------------
Subscribe to RHSM using username and password and attach to a pool


```
---
- name: Subscribe to RHSM
  hosts: rhsm
  remote_user: root
  gather_facts: no

  vars:
    gluster_repos_username: <user>@redhat.com
    gluster_repos_password: <passwd>
    gluster_repos_disable_all: true
    gluster_repos_pools: 9c31g9713e3adareak203r3adfa4e950
    gluster_repos_rhsmrepos:
       - rhel-7-server-rpms
       - rh-gluster-3-for-rhel-7-server-rpms
       - rh-gluster-3-nfs-for-rhel-7-server-rpms
       - rhel-ha-for-rhel-7-server-rpms
  roles:
    - gluster.repos
```