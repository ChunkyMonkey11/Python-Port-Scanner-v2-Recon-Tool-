from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QFileDialog
)
# from scanner.host_discovery import discover_hosts
# from scanner.port_scanner import scan_ports
import json, csv

class PortScannerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReconRaptor – Network Recon Suite")
        self.setGeometry(100, 100, 800, 600)

        # Layout
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        self.subnet_input = QLineEdit()
        self.subnet_input.setPlaceholderText("Enter Subnet (e.g. 192.168.1.0/24)")
        self.scan_button = QPushButton("Scan Network")
        self.scan_button.clicked.connect(self.scan_network)

        input_layout.addWidget(QLabel("Target Subnet:"))
        input_layout.addWidget(self.subnet_input)
        input_layout.addWidget(self.scan_button)

        self.host_table = QTableWidget(0, 1)
        self.host_table.setHorizontalHeaderLabels(["Live Hosts"])
        self.host_table.cellClicked.connect(self.scan_selected_host)

        self.result_table = QTableWidget(0, 2)
        self.result_table.setHorizontalHeaderLabels(["Port", "Service Banner"])

        export_layout = QHBoxLayout()
        self.export_json_btn = QPushButton("Export JSON")
        self.export_csv_btn = QPushButton("Export CSV")
        self.export_json_btn.clicked.connect(self.export_json)
        self.export_csv_btn.clicked.connect(self.export_csv)
        export_layout.addWidget(self.export_json_btn)
        export_layout.addWidget(self.export_csv_btn)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(QLabel("Discovered Devices"))
        main_layout.addWidget(self.host_table)
        main_layout.addWidget(QLabel("Open Ports for Selected Host"))
        main_layout.addWidget(self.result_table)
        main_layout.addLayout(export_layout)
        self.setLayout(main_layout)

        self.scan_results = {}

    def scan_network(self):
        subnet = self.subnet_input.text()
        hosts = discover_hosts(subnet)
        self.host_table.setRowCount(len(hosts))
        for i, ip in enumerate(hosts):
            self.host_table.setItem(i, 0, QTableWidgetItem(ip))

    def scan_selected_host(self, row, col):
        ip = self.host_table.item(row, 0).text()
        results = scan_ports(ip)
        self.scan_results[ip] = results
        self.result_table.setRowCount(len(results))
        for i, (port, banner) in enumerate(results):
            self.result_table.setItem(i, 0, QTableWidgetItem(str(port)))
            self.result_table.setItem(i, 1, QTableWidgetItem(banner))

    def export_json(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save JSON", "", "*.json")
        if path:
            with open(path, "w") as f:
                json.dump(self.scan_results, f, indent=2)

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "*.csv")
        if path:
            with open(path, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["IP", "Port", "Banner"])
                for ip, ports in self.scan_results.items():
                    for port, banner in ports:
                        writer.writerow([ip, port, banner])
