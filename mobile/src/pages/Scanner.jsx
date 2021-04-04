import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';
import { usePermissions, CAMERA } from 'expo-permissions';

import { Button } from 'react-native-elements';
import { BarCodeScanner } from 'expo-barcode-scanner';


export default function Scanner() {
  const [permissions, askForPermission] = usePermissions(CAMERA);

  return (
    <View>
      {permissions && permissions.status === 'granted'?
        <View>
          <BarCodeScanner
            onBarCodeScanned={({ type, data }) => console.log(type, data)}
            type="back"
            barCodeTypes={[BarCodeScanner.Constants.BarCodeType.qr]}
            style={[StyleSheet.absoluteFillObject, styles.scanner]}
          />
        </View>
        :
        <View>
          <Text>Нет разрешения на использование камеры</Text>
          <Button title="Выдать разрешение" onPress={askForPermission}/>
        </View>
      }
    </View>
  );
}

const styles = StyleSheet.create({
  scanner: {
    position: 'absolute',
    top: -20,
    width: Dimensions.get('window').width,
    height: Dimensions.get('window').height
  }
});
