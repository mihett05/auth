import React from 'react';
import { useLocation } from 'react-router-native';

import { Header, ThemeProvider } from 'react-native-elements';
import { StatusBar } from 'expo-status-bar';

const titles = {
  '/login': 'Вход',
  '/register': 'Регистрация',
  '/scanner': 'Сканировать'
};

export default function Layout({ children }) {
  const location = useLocation();

  return (
    <ThemeProvider>
      <Header centerComponent={{ text: titles[location.pathname] || 'Сканер', style: { color: '#fff' } }}/>
      {children}
      <StatusBar style="auto" />
    </ThemeProvider>
  );
}
