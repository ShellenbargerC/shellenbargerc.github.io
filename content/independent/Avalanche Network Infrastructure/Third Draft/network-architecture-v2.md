# Avalanche Operational Security - Network Architecture

Status: Draft 2 - Planned infrastructure, not yet implemented or tested

## Purpose

This document covers the technical infrastructure planned for Avalanche Operational Security. It explains the physical connections, server roles, access requirements, and backup design.

The business structure and daily workflows are covered in architecture-v2

## Physical Topology

The internet connection would connect to the firewall/router. The firewall/router would connect to the managed switch, which would provide the wired connections for the servers, workstations, wireless access point, printer, and smart laptop locker.

Crew laptops and guest devices would connect wirelessly through separate staff and guest wireless networks.

The current diagram shows physical connections. It does not yet show configured VLANs, IP addresses, routing, or firewall rules.

## Network Equipment

| Equipment | Connection | Purpose |
|---|---|---|
| Firewall / Router | Internet connection and managed switch | Internet connectivity, routing, and traffic control |
| Managed Switch | Firewall/router and wired endpoints | Connect devices and support VLAN separation |
| Wireless Access Point | Managed switch | Provide separate staff and guest wireless networks |
| Network Printer | Managed switch | Support staff printing |
| Smart Laptop Locker | Managed switch | Controlled laptop checkout and return |

The firewall/router would control traffic between network groups where it handles routing. The final routing arrangement is still being decided.

## Physical Servers

The design uses five separate physical servers. Each would have its own wired connection to the managed switch.

| Server | Planned role |
|---|---|
| Business File Server | Store proposals, network diagrams, installation instructions and guides, and device configurations |
| Security Server | Store penetration testing findings and reports |
| Finance Server | Store payroll and financial records |
| Operations Server | Host scheduling, job assignment, and laptop checkout services |
| Backup Server | Collect and store protected backups from all four working servers using RAID 6 storage |

Physical separation would not replace network restrictions or permissions within each server.

Hardware specifications, operating systems, storage capacities, and service software are still being decided. Hardware redundancy and availability arrangements for the working servers have not been designed yet.

## Workstations and Wireless Devices

| Device | Connection | Planned use |
|---|---|---|
| Owner's Office Computer | Wired to managed switch | Access company data and review business records |
| Administrator Computer | Wired to managed switch | Manage network equipment and servers |
| Office Operations Workstation | Wired to managed switch | Scheduling, assignments, and client coordination |
| Finance Workstation | Wired to managed switch | Payroll and financial work |
| Security Workstation | Wired to managed switch | Access findings and create penetration testing reports in the office |
| Crew Laptops | Staff Wi-Fi while in the office | Receive approved job files for offline use at client sites |
| Guest Devices | Guest Wi-Fi | Visitor connectivity; exact access rules still being decided |

The owner and administrator computers would be separate physical workstations.

The diagram uses representative workstations rather than showing a separate computer for every employee. The applications needed on employee computers and crew laptops are still being decided.

## Network Separation

The initial design identified staff, guest, server, and management groups. The expanded design now includes separate physical servers for business files, security reports, finance, operations, and backups.

The final VLAN boundaries and IP addressing plan are still being decided. Diagram colors identify roles and functions, not completed network isolation.

The design still needs to define:

- VLAN IDs and subnet sizes.
- Device addresses and default gateways.
- Switch port assignments.
- Access point connections and wireless network mappings.
- Where routing between network groups occurs.
- Firewall rules between groups.
- Backup network isolation.
- Management access to infrastructure.
- Guest internet access and restrictions on internal access.

Devices sharing a switch would not automatically be allowed to communicate with every other device.

## Data and Application Access

### Business File Server

Assigned crews would receive only the approved files needed for their client jobs. I would approve that access as the owner.

Permissions for other employees, access to client proposals, and when crew access is removed are still being decided.

### Security Server

Penetration testing findings and reports would be restricted to cyber security specialists while in the office, with an exception for me as the owner using my office computer.

Office operations would not have access. Reports would also be created in the office.

The technical controls for office-only access and the process for securely returning assessment data from client sites are still being decided.

### Finance Server

Payroll and financial records would be restricted to finance, with an exception for me as the owner.

### Operations Server

Office operations would manage the full schedule and job assignments.

The proposed employee view would show each employee's own scheduled work times. Finance would see work times needed for payroll without seeing client job details or worker destinations.

Detailed assignments would be released to crews when checking in at the office.

These restrictions would need application permissions as well as any network controls. Being allowed to connect to the Operations Server would not mean being allowed to read all of its data.

### Owner and Administrator Access

My office computer would have access to all company data areas.

The administrator computer would be used to manage systems. Who receives administrative accounts and what those accounts can change are still being decided.

Permission to view company data would be separate from permission to administer equipment, servers, or applications.

## Planned Communication Requirements

This table records required communication at a high level. It is not a completed firewall rule set.

| Source | Destination | Required purpose or restriction |
|---|---|---|
| Owner's Office Computer | Business File, Security, Finance, and Operations Servers | Access company data through authorized services |
| Office Operations Workstation | Operations Server | Manage schedules and assignments |
| Finance Workstation | Finance Server | Access payroll and financial records |
| Finance Workstation | Operations Server | Access payroll-related work times without job details or destinations |
| Security Workstation | Security Server | Access findings and create reports while in the office |
| Authorized crew-file preparation process | Business File Server and crew laptop | Prepare approved offline job files; process location and method undecided |
| Locker / Check-In Interface | Operations Server | Coordinate assignment checks and laptop checkout |
| Locker / Check-In Interface | Authentication service | Verify badge and fingerprint; service placement and integration undecided |
| Administrator Computer | Approved infrastructure management interfaces | Administer equipment and servers; exact permissions undecided |
| Backup Server | Each working server | Initiate scheduled backup collection |
| Working servers | Backup Server | Cannot initiate backup-storage connections; can respond to backup-initiated sessions |
| Backup system | Approved restore destination | Send selected restore data after administrator approval |

Protocols, ports, service accounts, and detailed permissions are still being decided. An undecided connection is not an approved connection.

## Smart Laptop Locker Integration

The smart laptop locker would connect to the managed switch. The check-in interface could be built into the locker or provided through a separate device.

The Operations Server would host assignment and checkout services. Authentication hosting and the exact integration with the locker are still being decided.

Before normal release, the system would check:

- The employee's company badge.
- The employee's fingerprint.
- Assignment to the job.
- Approval for the client files on the laptop.
- Laptop readiness.

Checkout would be recorded against the named employee collecting the shared crew laptop. Return would also be logged at the end of the day.

A returned laptop would remain unavailable until its returned files and readiness checks have been handled.

Loading job files, reviewing returned data, and removing old client files would be separate from the locker's physical release function.

### Authentication Recovery

If badge or fingerprint verification fails, normal release would be denied.

The proposed recovery process would require me to separately verify the employee's identity and approve a one-time release for that employee, laptop, and job.

This would not bypass approved file permissions or device readiness checks. Failed attempts and recovery approvals would be logged.

Fingerprint enrollment, protection of biometric records, recovery identity checks, and what happens if I am unavailable are still being decided.

## Backup Architecture

### Collection

The Backup Server would initiate scheduled pulls from:

- Business File Server.
- Security Server.
- Finance Server.
- Operations Server.

The working servers would not push backups or initiate access to backup storage. They could respond to sessions initiated by the Backup Server.

Collection protocols, backup accounts, and schedules are still being decided.

### Storage and Recovery Points

The Backup Server would use RAID 6 storage. RAID 6 requires at least four drives and can tolerate up to two drive failures.

Each working server would have its own independent history of five verified recovery points: the newest backup and the previous four.

Across the four working servers, this would normally mean 20 retained recovery points. Recovery points would not necessarily have equal storage sizes.

New backup jobs would not be allowed to overwrite or delete protected recovery points. The storage-enforced locking method and retention periods are still being decided.

### Rotation

A new recovery point would need to be created and verified before that source server's oldest eligible recovery point is removed.

Capacity planning would need to allow temporary space for a sixth recovery point for each server being backed up. More space may be required if older recovery points are still locked.

Failed backup jobs would not cause existing verified recovery points to be removed.

### Restores

An administrator would approve restores. The backup system would send the selected data to the original server or a replacement.

Working servers would not receive unrestricted access to pull data from backup storage.

Who can approve and perform restores, how restore destinations are authorized, and how recovery is tested are still being decided.

### Protection Limits

RAID 6 protects against drive failures. It does not prevent unwanted changes to files.

Pull-based collection, restricted backup access, and locked recovery points provide separate protections. Backup isolation may use a separate VLAN, host firewall rules, or both.

The backup scope covers all four working servers. Any additional systems would need their backup requirements reviewed.

## Supporting Services Still to Be Designed

The infrastructure still needs decisions about:

- Employee identities, authentication, and access groups.
- DNS and DHCP services.
- Time synchronization.
- Logging and monitoring.
- Software updates and device management.
- Authentication integration for the locker.
- Physical security and power protection.

These services are not yet assigned to servers or shown as separate devices in the diagram.

## Current Limitations

This is a planned architecture. No network configuration or simulation behavior has been implemented or tested yet.

The physical design currently shows one firewall/router, one managed switch, and one physical machine for each server role. Failover and redundancy beyond the Backup Server's RAID 6 storage have not been designed.

The simulation would use fictional company data, badge IDs, and fingerprint results. It would not collect actual biometric data.

A separate lab would be needed to validate equipment configuration, network isolation, storage permissions, RAID recovery, backup locking, and locker integrations.

## Next Technical Decisions

- Define the logical network groups and VLAN boundaries.
- Choose subnets, gateways, and addressing.
- Place supporting services.
- Define permitted communication using specific protocols and ports.
- Define administrative accounts and management access.
- Choose the controls for office-only security data access.
- Define backup isolation, schedules, retention, and recovery tests.
- Revise the diagram to show logical boundaries alongside physical connections.

## Project Ownership and AI Assistance

I developed Avalanche's business concept, drew the original network layout, and made the design decisions documented in this project. For Draft 2, I expanded the design to include separate physical servers, role-based access requirements, independent backup histories, and controlled laptop checkout.

I used ChatGPT to discuss and review the design, clarify questions, and help organize and revise the documentation. The updated diagram was generated with AI image editing based on my original drawing and the changes I directed.

This is a design project in progress. Implementation and testing will be documented as development continues.

## Network Design Decisions After Draft 2

### Routing Between VLANs

For the first Packet Tracer build, the firewall/router would handle routing between VLANs. The managed switch would provide the device connections and VLAN assignments.

The planned arrangement would use router-on-a-stick. One trunk connection between the managed switch and firewall/router would carry traffic for multiple VLANs. A separate router subinterface would provide the default gateway for each VLAN's subnet.

Connections for devices using a single VLAN would use switch access ports. The wireless access point connection and wireless network mappings are still being decided.

Traffic between VLANs would pass through the firewall/router, where the permitted connections would be defined. Traffic between devices within the same VLAN would not normally pass through the router. Restrictions within the same VLAN would need separate controls.

Network access would not replace file permissions or application permissions.

The earlier sections record the Draft 2 baseline. This decision establishes the routing arrangement for the first build. VLAN IDs, subnets, gateways, switch port assignments, router model, and specific traffic rules are still being decided. No configuration has been implemented or tested yet.


### Finance VLAN Boundaries

The Finance workstation and Finance Server would be placed in separate VLANs with separate IP subnets. Traffic between them would pass through the firewall/router using the planned router-on-a-stick arrangement.

Access rules would control which connections the Finance workstation can make to the Finance Server. Routing between the VLANs would not, by itself, restrict that access. The rules would need to be configured and tested.

This would provide a network control point for finance traffic. It would not replace authentication, application permissions, file permissions, or security controls on the workstation and server. It would not mean that all application content is inspected.

The VLAN IDs, subnet addresses, permitted services, ports, and administrative access rules are still being decided. Whether other devices share either of these VLANs has not been decided. This arrangement has not been implemented or tested yet.


### Security VLAN Boundaries

The Security workstation and Security Server would be placed in separate VLANs with separate IP subnets. Traffic between them would pass through the firewall/router using the planned router-on-a-stick arrangement.

Access rules would control which connections the Security workstation can make to the Security Server. Routing between the VLANs would not, by itself, restrict that access. The rules would need to be configured and tested.

The existing office-only access requirement for cyber security specialists would remain, with an exception for the owner using the owner's office computer. VLAN separation would provide a network control point, but would not by itself verify the employee's identity or establish all of the required office-only controls. Authentication, application permissions, file permissions, and endpoint controls still need to be defined.

The VLAN IDs, subnet addresses, permitted services, ports, and administrative access rules are still being decided. Whether other devices share either of these VLANs has not been decided. This arrangement has not been implemented or tested yet.


### Business File and Operations VLAN Boundaries

The Business File Server and Operations Server would be placed in VLANs separate from employee computers, using separate IP subnets from those computers. Employee traffic to these servers would pass through the firewall/router using the planned router-on-a-stick arrangement.

Access rules would control the permitted workstation-to-server connections. File permissions and application permissions would still control access to client files, schedule information, assignments, and checkout functions.

Whether the Business File Server and Operations Server share a server VLAN or use separate VLANs has not been decided. The VLAN IDs, subnet addresses, permitted services, ports, and the location of the approved crew-file preparation process are still being decided. This arrangement has not been implemented or tested yet.


### Dedicated VLANs for All Five Servers

Each physical server would use its own VLAN and IP subnet. These server VLANs would be separate from employee workstation networks.

| Server | Planned network boundary |
|---|---|
| Business File Server | Dedicated Business File Server VLAN and subnet |
| Security Server | Dedicated Security Server VLAN and subnet |
| Finance Server | Dedicated Finance Server VLAN and subnet |
| Operations Server | Dedicated Operations Server VLAN and subnet |
| Backup Server | Dedicated Backup Server VLAN and subnet |

Traffic between the server VLANs would pass through the firewall/router using the planned router-on-a-stick arrangement. Access rules would define the permitted connections. VLAN separation and routing would not, by themselves, authorize or block those connections.

This decision resolves the earlier question about whether the Business File Server and Operations Server would share a server VLAN. They would use separate VLANs.

The Backup Server would still initiate scheduled collection from the four working servers. The working servers would not be allowed to initiate connections to backup storage, but could respond to backup-initiated sessions. The selected traffic controls would need to distinguish new connections from permitted return traffic. Approved restores would still be initiated by the backup system.

A dedicated backup VLAN would be part of the isolation design. Host firewall rules and storage permissions still need to be defined.

VLAN IDs, subnet addresses, gateways, permitted services, and specific traffic rules are still being decided. This arrangement has not been implemented or tested yet.


### Guest Network Restrictions

Guest Wi-Fi would use a dedicated guest VLAN and IP subnet, separate from internal company networks. Guest devices would be allowed to access the internet, while access to internal company networks would be blocked.

The restrictions would cover company server networks, employee networks, backup storage, the printer, the smart laptop locker, and infrastructure management interfaces. Guest devices would not be allowed to administer the firewall/router, managed switch, or wireless access point.

The guest network would still need basic services for internet connectivity, including address assignment, name resolution, and access to its default gateway for forwarding internet traffic. These limited functions would not grant access to company applications or management interfaces. The service locations and narrowly scoped exceptions are still being decided.

The final rules would need to cover all internal company subnets. Guest internet traffic would use the firewall/router. The external connection and any required address translation are still being decided.

The guest VLAN ID, subnet, wireless equipment, wireless configuration, and specific access rules have not been selected. Isolation between guest devices on the same wireless network is a separate decision. This arrangement has not been implemented or tested yet.


### Password-Protected Guest Wi-Fi

Guest Wi-Fi would require a password provided to guests visiting the office. It would not be an open wireless network. The existing guest internet-only policy and restrictions on internal access would remain.

A wireless password would control admission to the guest network. It would not establish that a device is physically inside the office, since wireless coverage could extend outside the building. A nearby device with valid credentials could still connect.

The wireless authentication method, password rotation, and any individual or temporary guest credentials are still being decided. The selected Packet Tracer wireless equipment would need to support the authentication method used in the lab.

### Crew Laptop VLAN Boundary

Crew laptops would use a dedicated VLAN and IP subnet while connected to the company network. This network would be separate from office workstation networks, guest Wi-Fi, and all five server VLANs.

Traffic between crew laptops and other company VLANs would pass through the firewall/router using the planned router-on-a-stick arrangement. Access rules would limit the permitted connections.

The staff wireless network used by crew laptops would map to the crew laptop VLAN. The access point model, wireless configuration, and switch connection arrangement are still being decided.

The existing approved job-file preparation, offline use, return processing, and readiness requirements would remain. Placing a laptop in this VLAN would not by itself verify that the device is ready or that its files are approved. A separate quarantine or readiness network has not been selected.

The crew laptop VLAN ID, subnet, wireless authentication, internet access policy, permitted services, and connections for transferring approved or returned job files are still being decided. This arrangement has not been implemented or tested yet.


### Internal Crew Laptop File Transfers

The required job-file transfers would be between crew laptops and the internal Business File Server. This would require an approved internal communication path, rather than internet access.

The crew laptop network and Business File Server network would remain in separate VLANs. Any direct connections between them would pass through the firewall/router and would need explicit access rules for the selected transfer service.

Whether the laptop connects directly to the Business File Server or an authorized preparation process transfers files on its behalf is still being decided. The transfer protocol, ports, initiating device, employee or service identity, and file permissions have not been selected.

The existing owner approval of job files, offline use, returned-file review, and laptop readiness requirements would remain. Network connectivity would not grant access to all client files or authorize returned files to overwrite master records.

Internet access is not required for this file-transfer purpose. The broader crew laptop internet policy, including software updates and other uses, remains undecided. This workflow has not been implemented or tested yet.


### Authorized Technical Employee for File Preparation and Review

An authorized technical employee would prepare approved job files for crew laptops and review returned files. The owner would still approve which client files a crew is allowed to receive.

The technical employee would need permissions for the approved preparation and review process. This responsibility would not automatically grant network administration rights, unrestricted access to all client files, or access to Finance and Security Server data.

Returned files would not automatically overwrite master records. The review process, authority to update master records, and remaining laptop readiness checks still need to be defined.

The workstation or service used for preparation, transfer method, accounts, file permissions, and required network connections are still being decided. This workflow has not been implemented or tested yet.


### Smart Laptop Locker VLAN Boundary

The smart laptop locker would use a dedicated VLAN and IP subnet, separate from employee computer networks and all five server VLANs.

Connections from the locker to the Operations Server and authentication services would pass through the firewall/router. Access rules would limit the permitted connections to the services needed for the approved checkout and return workflow.

This separation would not replace badge and fingerprint verification, assignment checks, owner approval of client files, laptop readiness checks, or checkout and return logging. The authentication service location and integration are still being decided.

Whether a separate check-in screen is needed, and which network it would use, have not been decided. The locker VLAN ID, subnet, gateway, management access, protocols, ports, and specific traffic rules are still being decided. This arrangement has not been implemented or tested yet.

### Current Draft Checkpoint

The decisions added after Draft 2 establish central routing between VLANs, separate workstation and server networks, a dedicated VLAN for each of the five servers, password-protected guest internet access, a separate crew laptop network, internal job-file transfers, an authorized technical employee for file preparation and review, and a dedicated locker network. The existing office-only requirement for security findings and reports remains.

The next draft will hopefully complete the device-to-VLAN assignments, choose VLAN IDs and IP addressing, place supporting services, define permitted connections, select Packet Tracer equipment, map switch ports, and document the build sequence and expected test results.

No network configuration, access restriction, locker integration, or backup behavior has been implemented or tested yet.