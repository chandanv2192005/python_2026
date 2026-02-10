from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Determine protocol name
        protocol_name = ""
        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Other"

        print(f"Protocol: {protocol_name} | Source: {src_ip} -> Destination: {dst_ip}")

        # Check for payload
        if TCP in packet:
            payload = packet[TCP].payload
            if payload:
                print(f"   Payload (truncated): {str(payload)[:50]}...")
        elif UDP in packet:
            payload = packet[UDP].payload
            if payload:
                print(f"   Payload (truncated): {str(payload)[:50]}...")

def main():
    print("--- Network Packet Analyzer ---")
    print("Capturing packets... Press Ctrl+C to stop.")
    # sniff(prn=packet_callback, store=0)
    sniff(prn=packet_callback, count=10)

if __name__ == "__main__":
    main()
