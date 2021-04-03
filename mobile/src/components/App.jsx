import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { NativeRouter, Route, Link } from 'react-router-native';

import { ThemeProvider, Header } from 'react-native-elements';

import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import AppLoading from 'expo-app-loading';

import Home from '../pages/Home';



export default function App() {
  return (
    <SafeAreaProvider>
      <NativeRouter>
        <ThemeProvider>
          <Header centerComponent={{ text: 'Вход', style: { color: '#fff' } }}/>

          <Route exact path="/" component={Home} />
          <StatusBar style="auto" />
        </ThemeProvider>
      </NativeRouter>
    </SafeAreaProvider>
  );
}

