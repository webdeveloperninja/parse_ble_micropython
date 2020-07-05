from digi import ble
import time

ble.active(True)

scanner = None

# GAP is an acronym for the Generic Access Profile
scanner = ble.gap_scan(30000, interval_us=50000, window_us=50000)
scanner.stop()

with ble.gap_scan(30000, interval_us=50000, window_us=50000) as scanner:
    for adv in scanner:
        payload_bytes = adv['payload']
        payload = str(payload_bytes, 'utf-8')
        address_bytes = adv['address']

        print(payload)
        print(address_bytes)

        time.sleep(5)
