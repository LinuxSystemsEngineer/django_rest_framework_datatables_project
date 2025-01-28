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
    DROP TABLE IF EXISTS vlans_coresubnets;
''')

# Create the table
cursor.execute('''
    CREATE TABLE vlans_coresubnets (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        core VARCHAR(255),
        subnets VARCHAR(255),
        vlan_name VARCHAR(255),
        vlan_id INTEGER,
        guest_vrf_local VARCHAR(255),
        switch_port_pri VARCHAR(255),
        guest_vrf_sc VARCHAR(255),
        switch_port_sec VARCHAR(255),
        dhcp VARCHAR(255)
    )
''')

# Initialize Mimesis with a specific locale
m = Generic(locale=Locale.EN)

# Function to generate a random private IP address
def generate_private_ip():
    ip_range = random.choice([
        ("10.0.0.0", "255.0.0.0"),        # Class A private IP range
        ("172.16.0.0", "255.240.0.0"),    # Class B private IP range
        ("192.168.0.0", "255.255.0.0")    # Class C private IP range
    ])
    ip_address = m.internet.ip_v4()
    subnet_mask = ip_range[1]
    return ip_address, subnet_mask

# Generate 4094 fake records with sequential VLAN IDs
for vlan_id in range(1, 4095):
    core = m.food.fruit()                    # Using fruits for core
    subnets, subnet_mask = generate_private_ip()
    vlan_name = m.food.vegetable()           # Using vegetables for VLAN names
    guest_vrf_local = m.address.country()    # Using country names for guest VRF local
    switch_port_pri = m.internet.ip_v4()
    guest_vrf_sc = m.hardware.manufacturer() # Using manufacturer for guest VRF SC
    switch_port_sec = m.internet.ip_v4()
    dhcp = random.choice(["True", "False"]) # Randomly choosing DHCP status
    
    # Insert the record into the database
    cursor.execute('''
        INSERT INTO vlans_coresubnets (core, subnets, vlan_name, vlan_id, guest_vrf_local, switch_port_pri, guest_vrf_sc, switch_port_sec, dhcp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (core, subnets, vlan_name, vlan_id, guest_vrf_local, switch_port_pri, guest_vrf_sc, switch_port_sec, dhcp))

# Commit the changes and close the connection
conn.commit()
conn.close()

