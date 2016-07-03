## Solution Notes

**DYNAMIC FIREWALL**

- Vijay Prasad N
- Elangovan D
- Sathiskumar N
- Rajarajeswari R
- Smitha Raviprakash


## Problem Statement 

To build a Dynamic Firewall application that recieves feeds from open source feeds such as, Spamhause and Phishtank.

**Note**: Whitelist and blacklist domains are mandatory.


## Solution Approach

- Dynamic Firewall application fetches the blacklist IP addresses from Spamhaus
and Phishtank site on regular intervals.

- Based on the timestamp of retrieval, the IP address is identified as a blacklist or a whitelist.

- This IP address is passed to Ryu Faucet code, the validation of the IP address is done, and then flow is added with the corresponding action.

- The Flow is matched with the source IP address or the Destination IP address.

- Depending on the matched action the packets are dropped or forwarded.

## Deployment



1. Dynamic Firewall is integrated with the Ryu-Faucet controller.
2. Config to retrieve the black list from Spamhaus and Phishtank, is configurable.
3. Duration time to fetch the IP address from spamhaus and phishtank site, is also configurable.
4. Ryu-Faucet installation brings the firewall application along with the configs.

