import React from 'react';
import './style.css'
import WelcomeComponent from '../../components/WelcomeComponent';
import RecruitementComponent from '../../components/RecruitementComponent';
import AddDetailsComponent from '../../components/AddDetailsComponent';
const AddDetailsPage = () => {
  return (
    <div className="welcome-page">
      <WelcomeComponent ChildComponent={RecruitementComponent}/>
      <AddDetailsComponent/>
    </div>
  );
};

export default AddDetailsPage;
