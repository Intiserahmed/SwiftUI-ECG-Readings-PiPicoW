//
//  ContentView.swift
//  EcgVisualizationSwiftUI
//
//  Created by intiser Ahmed on 05/03/2024.
//

import SwiftUI

struct ContentView: View {
    @StateObject var bluetoothManager = BluetoothManager()

    var body: some View {
        Text("ECG Value: \(bluetoothManager.ecgValue)")
    }
}

#Preview {
    ContentView()
}
