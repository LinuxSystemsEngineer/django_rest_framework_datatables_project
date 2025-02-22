#!/usr/bin/env python3

import sqlite3
from mimesis import Generic
from mimesis.enums import Locale
import random

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Drop the table if it exists
cursor.execute('''
    DROP TABLE IF EXISTS vlans_vlans;
''')

# Create the table
cursor.execute('''
    CREATE TABLE vlans_vlans (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        vlan INTEGER,
        i_sid VARCHAR(255),
        name VARCHAR(255),
        subnet VARCHAR(255),
        subnet_mask VARCHAR(255),
        default_gateway VARCHAR(255),
        vrrp_ip_address_1 VARCHAR(255),
        vrrp_ip_address_2 VARCHAR(255),
        vrf VARCHAR(255),
        dhcp BOOLEAN,
        dhcp_server_1 VARCHAR(255),
        dhcp_server_2 VARCHAR(255),
        notes TEXT
    )
''')

# Initialize Mimesis with a specific locale
m = Generic(locale=Locale.EN)

# Function to generate a random private IP address and corresponding subnet mask
def generate_private_ip():
    ip_range = random.choice([
        ("10.0.0.0", "255.0.0.0"),         # Class A private IP range
        ("172.16.0.0", "255.240.0.0"),     # Class B private IP range
        ("192.168.0.0", "255.255.0.0")     # Class C private IP range
    ])
    ip_address = m.internet.ip_v4()
    subnet_mask = ip_range[1]
    return ip_address, subnet_mask

# Generate 4094 fake records with sequential VLAN IDs
for vlan_id in range(1, 4095):
    i_sid = m.food.fruit()               # Using fruits as unique identifiers
    name = m.food.vegetable()            # Using vegetables for names
    subnet, subnet_mask = generate_private_ip()
    default_gateway = m.internet.ip_v4()
    vrrp_ip_address_1 = m.internet.ip_v4()
    vrrp_ip_address_2 = m.internet.ip_v4()
    vrf = m.hardware.manufacturer()          # Using occupation names for VRF
    dhcp = random.choice([True, False])
    dhcp_server_1 = m.internet.ip_v4()
    dhcp_server_2 = m.internet.ip_v4()
    notes = m.food.dish()                # Using dish names for notes

    # Insert the record into the database
    cursor.execute('''
        INSERT INTO vlans_vlans (vlan, i_sid, name, subnet, subnet_mask, default_gateway, vrrp_ip_address_1, vrrp_ip_address_2, vrf, dhcp, dhcp_server_1, dhcp_server_2, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (vlan_id, i_sid, name, subnet, subnet_mask, default_gateway, vrrp_ip_address_1, vrrp_ip_address_2, vrf, dhcp, dhcp_server_1, dhcp_server_2, notes))

# Commit the changes and close the connection
conn.commit()
conn.close()

