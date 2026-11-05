# Avalanche Operational Security - Network Architecture

Status: Draft 4 - Planned infrastructure, not yet implemented or tested

## Purpose

This document covers the technical infrastructure planned for Avalanche Operational Security. It explains the physical connections, server roles, access requirements, and backup design.

The business structure and daily workflows are covered in architecture-v2

## New in Draft 4 - Packet Tracer Build Planning

Status: Draft 4 planning checkpoint complete - Implementation and testing pending

This network architecture document supports company design Draft 4. The previous design content is retained below. This section records the decisions for the next Packet Tracer build.

### Workstation and Crew Laptop Inventory

The first Packet Tracer build would include seven wired computers and three crew laptops. Proposed device names would identify each device in the topology and configuration notes.

| Proposed device name | Device role | Connection |
|---|---|---|
| PC-OWNER-01 | Owner's Office Computer | Wired to managed switch |
| PC-OPS-01 | Office Operations Workstation | Wired to managed switch |
| PC-FIN-01 | Finance Workstation | Wired to managed switch |
| PC-SEC-01 | Security Specialist Workstation 1 | Wired to managed switch |
| PC-SEC-02 | Security Specialist Workstation 2 | Wired to managed switch |
| PC-SEC-03 | Security Specialist Workstation 3 | Wired to managed switch |
| PC-ADMIN-01 | Administrator Computer | Wired to managed switch |
| LAP-CREW-01 | Field Crew 1 Laptop | Staff Wi-Fi while in the office |
| LAP-CREW-02 | Field Crew 2 Laptop | Staff Wi-Fi while in the office |
| LAP-SPARE-01 | Spare Crew Laptop | Staff Wi-Fi when connected in the office |

The three security workstations would replace the single representative security workstation in the earlier physical diagram. The crew laptop count would expand the earlier representative laptop to two assigned devices and one spare.

The existing five physical servers, firewall/router, managed switch, wireless access point, printer, smart laptop locker, and representative guest device would remain in the planned topology. Supporting services and any additional equipment still need to be placed.

Crew laptops would remain in the dedicated crew laptop VLAN when connected to staff Wi-Fi. Adding three security workstations would not by itself create three separate security workstation VLANs; the final device-to-VLAN table still needs to be completed.

The spare laptop would remain subject to assignment, file approval, checkout, and readiness checks before release. A spare device would not receive unrestricted access to company networks.

VLAN IDs, IP addresses, DHCP arrangements, switch port assignments, and Packet Tracer device models are still being decided. No configuration has been implemented or tested yet.

### DHCP and Static Address Assignment

Everyday office workstations, crew laptops, and guest devices would receive IP settings through DHCP. The owner's office computer, administrator computer, servers, infrastructure interfaces, printer, and smart laptop locker would use static addressing.

| Device or interface | Planned address assignment |
|---|---|
| PC-OPS-01 | DHCP |
| PC-FIN-01 | DHCP |
| PC-SEC-01, PC-SEC-02, and PC-SEC-03 | DHCP |
| LAP-CREW-01, LAP-CREW-02, and LAP-SPARE-01 | DHCP |
| Guest devices | DHCP |
| PC-OWNER-01 | Static |
| PC-ADMIN-01 | Static |
| Business File, Security, Finance, Operations, and Backup Servers | Static |
| Router VLAN gateway interfaces | Static |
| Managed switch and wireless access point management interfaces | Static |
| Network printer | Static |
| Smart laptop locker | Static |

Each DHCP-served VLAN would need an address pool and the appropriate subnet mask, default gateway, and DNS settings. Static addresses would be excluded from DHCP allocation to prevent overlapping assignments.

DHCP would assign network settings within the device's network. It would not determine the device's role, place it into the correct VLAN by itself, or grant application access. Static addresses would provide predictable destinations, but would not by themselves verify device or employee identity.

The DHCP service location, pool ranges, lease settings, DNS service location, and exact static addresses are still being decided. If DHCP is hosted outside a client VLAN, the design would need a supported relay arrangement and the required communication rules.

The router's external address would depend on the selected simulated internet connection and is not decided by this internal addressing policy. No address configuration has been implemented or tested yet.

### Router-Hosted DHCP

The firewall/router would provide DHCP for the first Packet Tracer build. It would use a separate DHCP pool for each VLAN requiring automatic address assignment.

Each pool would provide addresses from that VLAN's subnet, with the appropriate subnet mask, router gateway, and selected DNS settings. The guest pool would provide guest network settings without granting access to internal company services.

Because the router would host DHCP and have a gateway interface in each client VLAN, a separate server and DHCP relay would not be required for these directly connected VLANs. This resolves the earlier open question about DHCP service location.

Static infrastructure addresses, the owner's office computer address, and the administrator computer address would remain excluded from DHCP allocation. The final pool ranges, lease settings, DNS addresses, VLAN IDs, and subnet addresses are still being decided.

DHCP availability would depend on the router. Redundant DHCP and router failover are outside the current first-build design. No DHCP configuration has been implemented or tested yet.

### Dedicated Infrastructure Server

The design would add a separate physical Infrastructure Server for internal DNS, time synchronization, and centralized logging. The planned server inventory would now contain six physical machines: Business File, Security, Finance, Operations, Infrastructure, and Backup.

The Infrastructure Server would connect to the managed switch and use its own VLAN, IP subnet, and static address. The proposed device name would be SRV-INFRA-01. This extends the existing dedicated server VLAN arrangement to the new server.

| Planned service | Purpose |
|---|---|
| Internal DNS | Resolve approved internal service names to IP addresses |
| Time synchronization using NTP | Provide a consistent time source for supported company devices |
| Centralized logging using Syslog | Collect supported device logs for troubleshooting and review |

The firewall/router would continue to provide DHCP. DHCP settings for internal client networks would reference the selected internal DNS address when the addressing plan is completed.

Permitted devices would need narrowly defined connections to the appropriate Infrastructure Server services. Access to one service would not authorize access to the server's other services or management interfaces. Devices would send supported logs to the server; permission to view or change collected logs would be defined separately.

Guest devices would remain subject to the internet-only policy and would not be given access to internal Infrastructure Server services. Guest name resolution would use a separately selected internet-facing DNS arrangement.

The Packet Tracer service configuration would need to be checked against the capabilities of the selected simulated devices. Logs and service behavior demonstrated in the lab would not establish full production monitoring or identity management.

Employee identities, employee authentication, and locker authentication have not been assigned to this server. The upstream DNS arrangement, authoritative time source, log sources, log retention, administrator permissions, backup coverage, and service recovery requirements are still being decided.

The physical diagram would need an additional server and switch connection. VLAN IDs, IP addresses, switch ports, and specific service access rules have not been configured or tested.

### Infrastructure Server Backup Coverage

The Infrastructure Server would be included in the Backup Server's scheduled pull-based collection. The backup scope would now cover Business File, Security, Finance, Operations, and Infrastructure.

Each source server would retain five independent verified recovery points: its newest verified point and the previous four. Across five source servers, this would normally total 25 retained recovery points. This updates the earlier four-source, 20-point baseline without changing its existing protection requirements.

The Backup Server would initiate collection from the Infrastructure Server. The Infrastructure Server could respond to those sessions, but would not be allowed to initiate connections to backup storage. Approved restores would be initiated by the backup system after administrator approval.

New collection jobs would not be allowed to overwrite protected recovery points. A new point would need to be created and verified before that source server's oldest eligible point is removed. Failed jobs would not remove existing verified points. Capacity planning would need room for a temporary sixth point for each source being backed up, and additional space where older points remain locked.

The Infrastructure Server's backup contents would cover the service configuration and retained logs needed for recovery. Exact files, software state, log retention, backup schedules, storage capacity, protection periods, and recovery tests are still being decided.

Backup coverage for router and switch configurations remains a separate open decision. The planned Infrastructure Server backup would not automatically capture the router-hosted DHCP configuration. No backup collection, protection, or restore behavior has been implemented or tested yet.

### Printer Access Requirements

Printing through the network printer would be limited to office computers. Crew laptop and guest network access to printing services would be blocked.

Office computer access would cover the owner's office computer, Office Operations workstation, Finance workstation, three Security workstations, and administrator computer. Permission to print would remain separate from permission to administer the printer.

The printer would retain its planned static address. Its VLAN placement, supported printing protocol, required ports, and management access rules are still being decided. Where printing crosses VLAN boundaries, the firewall/router would need rules permitting only the selected printing services from approved office networks.

This decision would not grant unrestricted access from the printer to office computers or servers. Sensitive print collection procedures and the capabilities demonstrated in Packet Tracer still need to be defined. No printing configuration or access rule has been implemented or tested yet.

### VLAN-Based IPv4 Addressing Pattern

The first Packet Tracer build would use the private IPv4 addressing pattern 10.10.<VLAN number>.0/24 for its internal VLAN subnets. Selected VLAN IDs would stay within the range 1 through 254 so the number can be used directly as the third address octet. This convention would not assign every ID in that range or select VLAN 1 for normal device use.

Each subnet would use a subnet mask of 255.255.255.0. Its router gateway would use the .1 address. The planned router-on-a-stick subinterface for that VLAN would hold this gateway address.

| Example setting for VLAN 20 | Address or value |
|---|---|
| Network address | 10.10.20.0/24 |
| Subnet mask | 255.255.255.0 |
| Router gateway | 10.10.20.1 |
| Usable device addresses | 10.10.20.1 through 10.10.20.254 |
| Broadcast address | 10.10.20.255 |

VLAN 20 is an example of the agreed pattern, not a confirmed role assignment. The final VLAN table would identify which role uses each selected number.

In a /24 subnet, the first three octets identify the network and the final octet identifies an address within it. The .0 address identifies the network and the .255 address is reserved for subnet broadcasts; neither would be assigned to a workstation or server. The .1 address would be reserved for the router gateway, leaving .2 through .254 for other assignments in that subnet.

For example, a device at 10.10.20.10/24 would treat 10.10.20.11 as local to its IP subnet, but would use its gateway to reach 10.10.30.10 in a different subnet. These examples assume the configured VLAN and IP subnet assignments match the design.

The matching VLAN and subnet numbers are a documentation convention. The switch port or wireless configuration would determine VLAN membership; the address pattern alone would not configure VLAN separation or access rules.

The existing DHCP and static address assignment decisions would remain. DHCP ranges and individual static addresses have not been selected, and static addresses would need to be excluded from DHCP pools. No addressing configuration has been implemented or tested yet.

### Dedicated Printer VLAN

The network printer would use a dedicated VLAN and IP subnet, separate from office workstation networks, crew laptops, guest Wi-Fi, server networks, and the smart laptop locker network. The printer would retain its planned static address.

Approved office computer connections to the printer would pass through the firewall/router using the planned router-on-a-stick arrangement. Access rules would permit the selected printing services from office networks. Printing access from the crew laptop and guest networks would remain blocked.

Printing permission would not grant access to printer management interfaces. Printer administration and any required supporting service connections would be defined separately. The printer would not receive unrestricted permission to initiate connections to company computers or servers.

The VLAN number, subnet, static printer address, switch port, printing protocol, and exact access rules are still being decided. This resolves the earlier open question about printer VLAN placement. No printer network configuration or access rule has been implemented or tested yet.

### Shared Security Workstation VLAN

PC-SEC-01, PC-SEC-02, and PC-SEC-03 would share one Security workstation VLAN and IP subnet. Each would receive its network settings through the router-hosted DHCP pool for that VLAN.

The Security Server would remain in its dedicated server VLAN and subnet. Security workstation connections to the server would pass through the firewall/router and would need the permitted service rules.

Traffic between the three Security workstations in the same VLAN would normally remain within that network and would not pass through the router. Grouping them would not grant unrestricted access to each other's files or management interfaces; endpoint permissions and any additional local controls still need to be defined.

This decision groups the three specialist workstations together. It does not combine their network with Finance, Office Operations, the owner, administrator, crew laptops, or server networks. The existing office-only findings and report requirements would remain.

The Security workstation VLAN number, subnet, DHCP range, switch ports, and specific traffic rules are still being decided. No configuration has been implemented or tested yet.

### Packet Tracer Build Environment

The installed Packet Tracer version reported for the first build is 9.0.1. Equipment choices, interface names, wireless options, and supported service configurations would be checked against that installation as the build plan is completed.

Recording the installed version would not establish that every planned company workflow can be implemented in Packet Tracer. Network behavior demonstrated in the lab and application or hardware behavior requiring separate validation would remain clearly identified.

### Remote Management Source Restriction

PC-ADMIN-01 would be the only computer permitted to remotely access management interfaces on company servers and network equipment in the first Packet Tracer build. Its planned static address would be used in the relevant source restrictions. Authorized administrative credentials would still be required.

The scope would include the firewall/router, managed switch, wireless equipment, and all six physical servers. Where the printer or smart laptop locker provides remote management interfaces, the same administrator-only source restriction would apply.

PC-OWNER-01 would retain approved business-data access, but would not receive remote management access. Other office computers, crew laptops, and guest devices would also be blocked from management interfaces. Existing office printing permissions would remain separate from printer administration.

A permitted source address would not establish employee identity or replace authentication. The supported management protocols, accounts, interface restrictions, and access rules still need to be selected and tested. Source filtering would need to be applied at the appropriate routed and device management control points.

This rule would restrict administrative sessions. It would not block separately approved backup collection, logging, DNS, time synchronization, or application traffic merely because those services run on managed devices. Each such connection would need its own defined purpose and permissions.

Physical console access would remain a separate recovery method. Administrative account protection and the console recovery procedure are still being decided. Placement of the administrator workstation and equipment management interfaces into VLANs still needs to be finalized. No remote management configuration has been implemented or tested yet.

### Two-Access-Point Wireless Arrangement

The first Packet Tracer build would use two wireless access points instead of the single representative access point in the earlier diagram. Each would have its own wired connection to the managed switch.

| Proposed device name | Wireless role | Planned switch connection |
|---|---|---|
| AP-CREW-01 | Staff Wi-Fi for the three crew laptops | Access port in the crew laptop VLAN |
| AP-GUEST-01 | Password-protected guest Wi-Fi | Access port in the guest VLAN |

Each access point would serve one wireless network mapped to its assigned VLAN. The selected access points would need to support this arrangement in Packet Tracer 9.0.1. Multiple wireless networks over a shared AP trunk would not be required for this first-build design.

The access points would provide wireless network access. The firewall/router would remain the VLAN gateway and DHCP provider, and would enforce routed access rules. The build would not introduce a second DHCP service or an additional routing layer on the access points.

Guest internet-only restrictions, internal access blocking, and password protection would remain. The crew network would remain separate from guest, office workstation, and server networks. Its general internet access policy remains undecided.

The access points would retain the planned static management addressing. Supported management placement and controls would need to be checked for the selected devices; the guest access point's management interface would need protection from guest devices, including any same-VLAN path that does not traverse the router.

Wireless models, network names, authentication settings, radio configuration, switch port numbers, static management addresses, and final access rules are still being decided. The physical layout would need one additional AP and switch connection. No wireless configuration has been implemented or tested yet.

### Administrator Computer in the Server Room

PC-ADMIN-01 would be physically located in the server room. It would remain separate from PC-OWNER-01 and everyday office workstations. The inventory would still contain seven wired computers; this decision changes the administrator computer's location rather than its count.

Its static addressing and administrator-only remote management role would remain. Physical placement would not by itself assign VLAN membership or change network access rules. Its final switch port and VLAN assignment still need to be documented.

Access to the administrator computer would require a badge, biometric verification, and a sign-in log. The enforcement point is not yet selected: the checks could apply to server room entry, computer sign-in, or both. Hardware, authentication integration, log contents, log storage, retention, and authorized users are still being decided.

Authorized administrative credentials would still be required for management sessions. Room access, workstation sign-in, and privileged system actions would be treated as separate events when defining the controls and evidence. This decision does not extend biometric requirements to other office computers.

The build documentation would distinguish the planned physical and authentication controls from the behavior actually demonstrated in Packet Tracer. These controls have not been implemented or tested.

### Two Separate Badge and Biometric Checkpoints

Badge and biometric verification would be required at both the server room door and PC-ADMIN-01 sign-in. These would be separate authentication checkpoints. Successful room entry would not authorize a workstation session or automatically grant administrative access.

Server room entry attempts and administrator workstation sign-in attempts would be recorded separately, including successful and failed attempts. The planned records would identify the checkpoint, claimed employee identity, timestamp, and outcome. Actual biometric samples or templates would not be placed in activity logs.

The exact readers, authentication services, log transport, storage location, retention, and review permissions still need to be selected. The existing Infrastructure Server logging role would not by itself establish that it can receive these physical access and workstation events. That integration would need separate validation.

Authorized administrative credentials would still be required for management sessions. Badge and biometric access checks would not replace authorization for a particular administrative task.

This resolves the earlier uncertainty about whether the checks apply to the door, workstation, or both. Enrollment, access revocation, lock behavior, failure recovery, and any exception approval process remain undecided. No authentication bypass is authorized by this decision.

The project would continue to use fictional badge IDs and simulated biometric outcomes. No actual biometric data would be collected. The documentation would distinguish planned controls from authentication and physical access behavior actually demonstrated in the lab.

### No Crew Laptop Internet Access on the Office Network

The crew laptop VLAN would not be allowed to access the internet through Avalanche's office network. This would apply to LAP-CREW-01, LAP-CREW-02, and LAP-SPARE-01 when connected to that network.

The firewall/router would block internet-bound traffic from the crew laptop network. Only explicitly approved internal service connections and their required return traffic would be permitted. No unrestricted access to office computers or server networks would be granted.

Required internal functions would include router-hosted DHCP and the approved job-file transfer workflow. Exact file-transfer connections, internal DNS needs, time synchronization, and any other supporting service access still need to be defined in the communication table. The existing crew printing restriction would remain.

The crew access point would provide network access in the crew VLAN, while the firewall/router would enforce the routed restrictions. Wireless configuration and endpoint controls would need to prevent unintended alternative paths; the VLAN rule alone would not control every possible connection on a laptop.

This resolves the earlier open question about crew laptop internet access on the office network. It does not define policy for client-site networks, other wireless networks, or internet access away from the office.

Software updates would require a separately designed controlled process. No temporary internet exception or update service has been selected. These restrictions and the update process have not been implemented or tested.

### End of Draft 4 Checkpoint

Draft 4 is complete as the current planning checkpoint. It establishes the expanded device inventory, router-hosted DHCP, static infrastructure addressing, VLAN-based /24 address pattern with .1 gateways, Infrastructure Server services and backup coverage, office-only printing, dedicated printer network, grouped Security workstations, separate crew and guest access points, administrator-only remote management, and office-network internet blocking for crew laptops.

It also records server room placement of PC-ADMIN-01, separate badge and biometric checks at room entry and workstation sign-in, and separate sign-in records. Physical access and authentication controls remain planned requirements rather than demonstrated Packet Tracer behavior.

The proposed direct file-transfer process in which the authorized technical employee signs into each crew laptop has not been approved. The employee's responsibility and owner approval of job-file access remain confirmed; the transfer path, protocol, account permissions, and returned-file review process still need to be finalized.

Before configuring the full topology, the next draft would produce the consolidated device-to-VLAN table, specific VLAN IDs, subnets, static addresses, DHCP ranges, switch port map, selected Packet Tracer models, and initial permitted-service and test tables. Management network placement and supported wireless management restrictions would be included in those decisions.

The next draft would begin building the basic Packet Tracer topology while the remaining service details are resolved. The initial sequence would place and cable the selected devices, configure a small set of VLANs and router gateways, test basic addressing, and then add the remaining networks and access rules in stages.

Office computer internet permissions, the controlled update process, simulated external services, final file-transfer method, authentication service placement, and the exact boundary between demonstrated and separately documented workflows remain open. These would be tracked without requiring every production integration to be completed before the first topology is built.

All earlier content has been preserved. Confirmed later decisions resolve the corresponding earlier open questions; unresolved items remain planned work. No network configuration, isolation test, backup test, physical access integration, or biometric integration has been implemented or validated in this draft.

## Previous Design Content

The following content is retained from the previous drafts. Where an older section leaves a question open or gives an earlier equipment count, the confirmed Draft 4 updates above take precedence. Unresolved questions remain open.

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

## Previously Established Network Design Decisions

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

### Previous Design Checkpoint

The decisions added after Draft 2 establish central routing between VLANs, separate workstation and server networks, a dedicated VLAN for each of the five servers, password-protected guest internet access, a separate crew laptop network, internal job-file transfers, an authorized technical employee for file preparation and review, and a dedicated locker network. The existing office-only requirement for security findings and reports remains.

The next draft will hopefully complete the device-to-VLAN assignments, choose VLAN IDs and IP addressing, place supporting services, define permitted connections, select Packet Tracer equipment, map switch ports, and document the build sequence and expected test results.

No network configuration, access restriction, locker integration, or backup behavior has been implemented or tested yet.