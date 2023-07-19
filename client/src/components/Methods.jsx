import React, {useState, useEffect} from 'react'
import {CardActionArea, CardActions } from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import {Button, Box, Paper, Grid, Typography, CssBaseline, ThemeProvider} from '@mui/material';
import Container from '@mui/material/Container'

function Methods() {
    /*------------------STATE--------------------*/
    //state for static method page
    const [nMethod, setN] = useState([])
    const [jMethod, setJ] = useState([])

    /*------------------STATE--------------------*/
    /*-------------------CRUD--------------------*/

    useEffect((e) => {
        fetch(`/api/nudges/1`)
        .then(res => res.json())
        .then(nMethod => setN(nMethod))
    },[])
    console.log(jMethod)

    useEffect((e) => {
        fetch(`/api/journals/1`)
        .then(res => res.json())
        .then(jMethod => setJ(jMethod))
    },[])
    console.log(jMethod)


    /*-------------------CRUD--------------------*/



  return (
    <div className="page">
    <Container >
    <Card sx={{ maxWidth: 900, maxHeight: 900, margin: 5  }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image={nMethod.image}
          alt={nMethod.action_type}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
          {nMethod.action_type}
          </Typography>
          <Typography variant="body2" color="text.secondary">
          {nMethod.description}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
    <Card sx={{ maxWidth: 900, maxHeight: 900, margin: 5 }}>
    <CardActionArea>
      <CardMedia
        component="img"
        height="140"
        image={jMethod.image}
        alt={jMethod.action_type}
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
        {jMethod.action_type}
        </Typography>
        <Typography variant="body2" color="text.secondary">
        {jMethod.description}
        </Typography>
      </CardContent>
    </CardActionArea>
  </Card>
  </Container>
  </div>
  )
}

export default Methods
    // <div>
    //     <h1>methods</h1>
    //     <div>
    //         <img src={nMethod.image} alt={nMethod.action_type}></img>
    //         <h3>{nMethod.action_type}</h3>
    //         <p>{nMethod.description}</p>
    //     </div>
    //     <div>
    //         <img src={jMethod.image} alt={jMethod.action_type}></img>
    //         <h3>{jMethod.action_type}</h3>
    //         <p>{jMethod.description}</p>
    //     </div>
    // </div>