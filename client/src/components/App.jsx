import React, { useContext, useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Home";
import Auth from "./Auth";
import About from "./About";
import Pillars from "./Pillars";
import ActionContainer from "./ActionContainer";
import NudgeAction from "./NudgeAction"
import Growth from "./Growth";
import RecContainer from "./RecContainer";
import Nav from "./Nav";
import Context from "./Context"
import Methods from "./Methods"
import ActionOptions from "./JournalAction"
import User from "./User"

import {Button, Paper, Grid, Typography, CssBaseline, ThemeProvider, Box} from '@mui/material';
import AppBar from '@mui/material/AppBar';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Container from '@mui/material/Container'
import theme from "../theme.jsx"

function App() {

/*------------------STATE--------------------*/

  //1. state of recommendations
  const [recs, setRecs] = useState([])

  //2. state of pillars
  const [pillars, setPillars] = useState([])

  //5. user state
  const [user, setUser] = useState(null)
 
/*------------------STATE--------------------*/
/*-------------------CRUD--------------------*/
useEffect(() => {
  getRecs()
  getPillars()
}, [user])


//separate user info and rest. useEffect run based on dependency array. whenever dependency changes, the useEffect runs
useEffect(() => {
  authorizeUser()
  getUser()
}, [])
 console.log(user)

  //1. rec fetch
  function getRecs(){
    fetch('/api/recommendations')
    .then(res => res.json())
    //1st instruction post rendering js obj:
    //grab state recs then UPDATE the state to BE the recs obj
    .then(recs => setRecs(recs))
  }

  //2. pillars fetch
  function getPillars(){
    fetch('/api/pillars')
    .then(res => res.json())
    .then(pillars => setPillars(pillars))
  }
 console.log(pillars)

  //5. login/logout/signup
  function authorizeUser(){
    if (user == null) {
      fetch('/api/authorize_session')
      .then(response => {
        if (response.ok) {
          response.json().then((user) => setUser(user))
        } else {
          setUser(null)
        }
      })
    }
  }

  // }, [user]);
  function getUser(){
    if (user && user.id) {
      fetch(`/api/users/${user.id}`)
        .then(res => res.json())
        .then(fetchedUser => {
          setUser(fetchedUser);
        });
    }
  }
  
  console.log(user);

/*-------------------CRUD--------------------*/
/*------------------CONST--------------------*/

  //2.map through pillars to access a single pillar and pass as props
  //note, accessing journal and nudge NOW as they are arrays
                        
                        
  const pillars_map = [...pillars].map(el => (
    <Grid item xs={6} >
        <Pillars key={el.id } pillar={el}/>
    </Grid>
  ))
    
  const pillar_list = <Routes><Route path="/pillars" element={pillars_map}/></Routes>
/*------------------CONST--------------------*/
/*----------------FUNCTION-------------------*/

    //5. sign up/log in/log out
    function updateUser(user) {
      setUser(user)
    }


  //   const navigate = useNavigate();
  //   function handleLogout() {
  //     fetch("/api/logout", {
  //       method: "POST",
  //     }).then((res) => {
  //       if (res.ok){
  //         updateUser(null);
  //         navigate("/home");
  //       }
  //     });
	// }
/*----------------FUNCTION-------------------*/


//THINK ABOUT ROUTES AND WHERE THEY TAKE YOU!!!!
  return (
    
        <div >
          {/* <ThemeProvider theme={theme} > */}
            <React.Fragment>
              {/* <CssBaseline /> */}
            </React.Fragment>
          <Context.Provider value={{user, setUser}}>
            <Router>
            <Nav updateUser={updateUser}/>
            <Routes>
              <Route path="/auth" element={<Auth updateUser={updateUser}/>} />
              <Route path='/users' element={<User setUser={setUser} updateUser={updateUser} user={user} />} />
              <Route path="/home" element={<Home/>} />
              <Route path="/about" element={<About/>} />
              <Route path="/methods/:pillar_id" element={<ActionContainer/>} />
              <Route path="/methods" element={<Methods/>} />
              <Route path="/methods" element={<ActionOptions />} />
              <Route path="/growth" element={<Growth/>} />
              {/*1. passing rec state to component*/}
              <Route path="/recommended" element={<RecContainer recs={recs}/>} />
              {/*2. passing pillar state to component*/}
              {/* <Route path="/pillars" element={pillars_map}/> */}
            </Routes>
            {/* columns={{ xs: 3, sm: 8, md: 8 }} */}
            <div className="page">
              <Grid  container spacing={{ xs: 1, md: 2 }} >
                  {pillar_list}
              </Grid>
            </div>
            </Router>
          </Context.Provider>
        
          {/* </ThemeProvider> */}
        </div>
    
  );


}

export default App;


/*-------------------DELIVERABLES--------------------*/

//1. make recommendations appear on the browser

//2. make pillars appear in the browser

//3. make methods/actions appear on the browser
//4. make action prompts appear on the browser
//5. sign up/log in/log out
//6. methods page


{/* <NavLink exact to = "/home">micelio</NavLink>
<NavLink exact to = "/auth">welcome</NavLink>
<NavLink exact to = "/about">about</NavLink>
<NavLink exact to = "/pillars">pillars</NavLink>

<NavLink exact to = "/methods">methods</NavLink>
<NavLink exact to = "/growth">growth</NavLink>
<NavLink exact to = "/nudge">nudge</NavLink>
<NavLink exact to = "/journal">journal</NavLink>

<NavLink exact to = "/recommended">recommended</NavLink> */}



//state for nudges and journals to 