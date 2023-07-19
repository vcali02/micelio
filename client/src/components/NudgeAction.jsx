import React, {useState, useEffect} from 'react'
import {useParams } from "react-router-dom";
import {CardActionArea, CardActions } from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import {Button, Box, Paper, Grid, Typography, CssBaseline, ThemeProvider} from '@mui/material';
import Container from '@mui/material/Container'

function NudgeAction({action}) {
    console.log(action.id)

    /*------------------STATE--------------------*/
    //4.action state
    const [selectAction, setSelectAction] = useState(true)

    //5. prompt state
    const [prompt, setPrompt] = useState([])

    /*------------------STATE--------------------*/
    /*-------------------CRUD--------------------*/
    
    useEffect((e) => {
        fetch(`/api/nprompts/${action.id}`)
        .then(res => res.json())
        .then(prompt => {
            setPrompt(prompt)
        })
    },[])
    
    /*-------------------CRUD--------------------*/
    /*------------------CONST--------------------*/
    let prompt_arr = Object.values(prompt)
   
    // const getRandomPrompt = () => {
    //     return prompt_arr[Math.floor(Math.random() * prompt_arr.length)]
    // }
    // console.log(getRandomPrompt())
    // getRandomPrompt()
    const ipickyou = prompt_arr[Math.floor(Math.random() * prompt_arr.length)]
    console.log(ipickyou)
   
    //3. mapping through nudge prompt to access individual nudge prompts
    // const nprompts = [...prompt_arr].map((el, i) => {
    //     return <NPrompts key={i} nprompts={el}/>
    // })
    // console.log(Object.values(prompt))

     /*------------------CONST--------------------*/
    /*-------------------FUNK--------------------*/
    function handleClick(e){
        setSelectAction(!selectAction)
    }
    /*-------------------FUNK--------------------*/
    



  return (
    <div>
        {selectAction ? (
    
    <Card sx={{ minWidth: 900, maxHeight: 900, margin: 5 }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image={action.image}
          alt={action.action_type}
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
          {action.action_type}
          </Typography>
          <Typography variant="body2" color="text.secondary">
          {action.description}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button onClick={(e) => handleClick(e)} sx={{marginLeft: "auto"}} size="small" color="primary">
          I pick...you!
        </Button>
      </CardActions>
    </Card>
     ) : (
    <Card>
        <CardContent >
        <Button onClick={(e) => handleClick(e)}>Back to Method</Button>
          <Typography>{ipickyou.action_prompt}</Typography>
      </CardContent>
    </Card>
    )}
    </div>
  )
}

export default NudgeAction