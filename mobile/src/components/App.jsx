import React from 'react';
import { NativeRouter, Route } from 'react-router-native';

import { SafeAreaProvider } from 'react-native-safe-area-context';
import Layout from './Layout';

import Home from '../pages/Home';
import Scanner from '../pages/Scanner';


export default function App() {
  return (
    <SafeAreaProvider>
      <NativeRouter>
        <Layout>
          <Route exact path="/" component={Home} />
          <Route path="/scanner" component={Scanner} />
        </Layout>
      </NativeRouter>
    </SafeAreaProvider>
  );
}

