import React from 'react'
import { View, Text, StyleSheet } from 'react-native';
import { useHistory } from 'react-router-native';

import { Button, Input } from 'react-native-elements';

import { Formik } from 'formik';

export default function Home() {
  const history = useHistory();

  return (
    <View>
      <Formik initialValues={{
        login: '',
        password: ''
      }} onSubmit={(values) => {}}>
        {({ handleChange, handleBlur, handleSubmit, values }) => (
          <View>
            <Input
              onChangeText={handleChange('login')}
              onBlur={handleBlur('login')}
              value={values.login}
              placeholder="Логин"
              label="Логин"
            />
            <Input
              onChangeText={handleChange('password')}
              onBlur={handleBlur('password')}
              value={values.password}
              placeholder="Пароль"
              label="Пароль"
              secureTextEntry
            />
            <Button onPress={handleSubmit} title="Войти" containerStyle={styles.button}/>
            <Button title="Создать аккаунт" onPress={() => history.push('/register')}/>
            <Button title="Скан" onPress={() => history.push('/scanner')}/>
          </View>
        )}
      </Formik>
    </View>
  );
}

const styles = StyleSheet.create({
  button: {
    marginBottom: 20,
  }
});
