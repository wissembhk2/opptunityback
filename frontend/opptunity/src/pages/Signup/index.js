import React from 'react';
import './style.css'
import FirstPageComponent from '../../components/WelcomeComponent/FirstPage';
import WelcomeComponent from '../../components/WelcomeComponent';
import SignupComponent from '../../components/SignupComponent';
const SignUpPage = () => {
  return (
    <div className="welcome-page">
      <WelcomeComponent ChildComponent={FirstPageComponent}/>
     <SignupComponent/>
    </div>
  );
};

export default SignUpPage;
