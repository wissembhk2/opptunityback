import React from 'react';
import './style.css'
import FirstPageComponent from '../../components/WelcomeComponent/FirstPage';
import WelcomeComponent from '../../components/WelcomeComponent';
import EmailConfirmationComponent from '../../components/EmailConfirmationComponent';
const EmailConfirmationPage = () => {
  return (
    <div className="welcome-page">
      <WelcomeComponent ChildComponent={FirstPageComponent}/>
      <EmailConfirmationComponent/>
    </div>
  );
};

export default EmailConfirmationPage;
