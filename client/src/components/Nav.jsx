import React, {useState} from 'react'
import DrawerComp from "./DrawerComp"
import { Link, useNavigate, NavLink, BrowserRouter } from "react-router-dom"
import PropTypes from 'prop-types';
import AppBar from '@mui/material/AppBar';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import {useTheme, useMediaQuery, Grid, Toolbar, Avatar, IconButton, Menu, Fade, MenuItem} from '@mui/material'
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import SpaIcon from '@mui/icons-material/Spa';
import { red } from '@mui/material/colors';


function Nav({updateUser, user}) {
    /*------------------STATE--------------------*/
    const theme = useTheme()
    const isMatch = useMediaQuery(theme.breakpoints.down('md'))

    const [value, setValue] = useState()
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl)





    
    const handleClick = (event) => {
        setAnchorEl(event.currentTarget)
    }

    const handleClose = () => {
        setAnchorEl(null)
    }
    
    const navigate = useNavigate();
    function handleLogout() {
		fetch("/api/logout", {
            method: 'POST',
        }).then((res) => {
			if (res.ok){
				updateUser(null);
				navigate("/home");
			}
		});
	}
    const login = <NavLink exact to="/auth"> LOG IN</NavLink>
    const logout = <NavLink exact to = "/home" onClick={handleLogout}> LOG OUT</NavLink>
    const profile = <NavLink exact to = "/users"> PROFILE </NavLink>
    const home = <NavLink exact to = "/home"> HOME </NavLink>
    const about = <NavLink exact to = "/about"> ABOUT</NavLink>
    const pillars = <NavLink exact to = "/pillars"> PILLARS </NavLink>
    const methods = <NavLink exact to = "/methods"> METHODS </NavLink>
    {/* <NavLink exact to = "/nudges">  </NavLink>
    <NavLink exact to = "/journals">  </NavLink> */}
    const growth = <NavLink exact to = "/growth"> GROWTH </NavLink>
    const recommended = <NavLink exact to = "/recommended"> RECOMMENDED</NavLink>


    return (
    <>
        <AppBar sx={{background: '#e9cfb4', backgroundSize: "900px"}}  >
            <Toolbar className="App-header">
        
            {isMatch? 
            <>
            <IconButton
                    onClick={handleClick}
                    size="small"
                    sx={{ ml: 2}}
                    aria-controls={open ? 'account-menu' : undefined}
                    aria-haspopup="true"
                    aria-expanded={open ? 'true' : undefined}
                >
                <Avatar sx={{ width: 65, height: 65, bgcolor: red[300] }}>
                    <SpaIcon/>
                </Avatar>
                </IconButton>
                <Menu
                    
                    indicatorColor="secondary" 
                    textColor="inherit"
                    id="fade-menu"
                    MenuListProps={{
                    'aria-labelledby': 'fade-button',
                    }}
                    anchorEl={anchorEl}
                    open={open}
                    onClose={handleClose}
                    TransitionComponent={Fade}
                >
                    <MenuItem onClick={handleClose}>{profile}</MenuItem>
                    <MenuItem onClick={handleClose}>{login}</MenuItem>
                    <MenuItem onClick={handleClose}>{logout}</MenuItem>
                </Menu>
            <DrawerComp home={home} about={about} pillars={pillars} methods={methods} growth={growth} recommended={recommended}/>
            </>
            :
                <Grid container sx={{marginLeft: "center"}}>
                <Grid item xs={3}>
                <IconButton
                    onClick={handleClick}
                    size="small"
                    sx={{ ml: 2 }}
                    aria-controls={open ? 'account-menu' : undefined}
                    aria-haspopup="true"
                    aria-expanded={open ? 'true' : undefined}
                >
                <Avatar sx={{ width: 65, height: 65, bgcolor: red[300] }}>
                    <SpaIcon/>
                </Avatar>
                </IconButton>
                <Menu
                    indicatorColor="secondary" 
                    textColor="inherit"
                    id="fade-menu"
                    MenuListProps={{
                    'aria-labelledby': 'fade-button',
                    }}
                    anchorEl={anchorEl}
                    open={open}
                    onClose={handleClose}
                    TransitionComponent={Fade}
                >
                    <MenuItem onClick={handleClose}>{profile}</MenuItem>
                    <MenuItem onClick={handleClose}>{login}</MenuItem>
                    <MenuItem onClick={handleClose}>{logout}</MenuItem>
                </Menu>
                </Grid>
                <Grid item xs={9}>
                <Tabs sx={{marginTop: "160px", marginLeft: "center"}} indicatorColor="secondary" textColor="secondary" value={value} onChange={(e, val)=>setValue(val)}>
                    {/* <Tab label={login}/>
                    <Tab label= {logout}/>
                    <Tab label= {profile}/> */}
                    <Tab label= {home}/>
                    <Tab label= {about}/>
                    <Tab label= {pillars}/>
                    <Tab label= {methods}/>
                    <Tab label= {growth}/>
                    <Tab label= {recommended}/>
                </Tabs>
                </Grid>
            </Grid>
            }
            
            </Toolbar>
        </AppBar>
    </>
        )
}

export default Nav


    // <NavLink exact to="/auth"> log in </NavLink> 
    // <NavLink exact to = "/home"> log out</NavLink>
    // <NavLink exact to = "/users"> profile </NavLink>
    // <NavLink exact to = "/home"> micelio </NavLink>
    // <NavLink exact to = "/about"> about</NavLink>
    // <NavLink exact to = "/pillars"> pillars </NavLink>
    // <NavLink exact to = "/methods"> methods </NavLink>
    // <NavLink exact to = "/nudges">  </NavLink>
    // <NavLink exact to = "/journals">  </NavLink>
    // <NavLink exact to = "/growth"> growth </NavLink>
    // <NavLink exact to = "/recommended"> recommended</NavLink>