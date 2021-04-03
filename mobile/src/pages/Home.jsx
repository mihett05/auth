import React from 'react'
import { View, Text } from 'react-native';

import { Button, Input } from 'react-native-elements';

import { Formik } from 'formik';

export default function Home() {
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
              securityTextEntry
            />
            <Input
              onChangeText={handleChange('password')}
              onBlur={handleBlur('password')}
              value={values.password}
              placeholder="Пароль"
              securityTextEntry
            />
            <Button onPress={handleSubmit} title="Войти"/>
          </View>
        )}
      </Formik>
    </View>
  );
}


