import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './web.css'
import './index.css'
import {Routes, Route} from "react-router-dom"
import WebFrame from './web.jsx';
import Features from './features.jsx';
import NearbyHall from './nearbyhall.jsx'
import Hall from './hall.jsx'
import setimg from './assets/img4.jpg'
import TSimg from './assets/ts4.jpg'
import APimg from './assets/AP4.jpg'
import ak from './assets/ak.jpg'
import hsb from './assets/hsb.jpg'
import abc from './assets/abc.jpg'
import sda from './assets/sda.jpg'
import pa from './assets/pa.jpg'
import monika from './assets/monika.jpg'

function App() {
  

  return (
    <>
    <Routes> {/* home page with your cards*/}
    <Route path='/' element={
      <>
     <WebFrame />
     <NearbyHall text={'Recommended halls, '} />
      <Features img={setimg} text='S.E.T  Mahal' to="/Hall/S.E.T Mahal"/>
      <Features img={TSimg} text='T.S Mahal' to="Hall/ T.S Mahal"/>
      <Features img={APimg} text='A.P Mahal' to="Hall/A.P Mahal"/>
      <NearbyHall text={'Recommended Cators, '} />
       <Features img={ak} text='A.K  Catering' to="/Hall/A.K Catering "/>
      <Features img={hsb} text='Saravana Bhavan caters' to="Hall/ Saravana Bhanvan caters"/>
      <Features img={abc} text='Asbath Bhai cook' to="Hall/Asbath Bhai cook"/>
      <NearbyHall text={'Recommended Decorors, '} />
       <Features img={sda} text='S.D.A Decoration' to="/Hall/S.D.A Decoration"/>
      <Features img={pa} text='P.A Decoration' to="Hall/ P.A Management"/>
      <Features img={monika} text='Monika Decoration' to="Hall/Monika Decors"/>
      <p style={{fontWeight:"normal" , textAlign:"center"}}>@all the rights and copyrights are bagged by praveenCorpts</p>
      <p style={{fontWeight:"normal" , textAlign:"center"}}>Terms and condition applies</p>
      </>
    }/>
    {/*dynamic hall page */}
    <Route path="/Hall/:slug" element={<Hall/>}/>
    </Routes>
    </>
  );
}

export default App;
