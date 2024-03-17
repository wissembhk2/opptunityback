import React from 'react';
import './style.css'
import FirstPageComponent from '../../components/WelcomeComponent/FirstPage';
import WelcomeComponent from '../../components/WelcomeComponent';
import SigninComponent from '../../components/SigninComponent';
const SignInPage = () => {
  return (
    <div className="welcome-page">
      <WelcomeComponent ChildComponent={FirstPageComponent}/>
     <SigninComponent/>
    </div>
  );
};

export default SignInPage;
