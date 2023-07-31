import React, {useState, useEffect} from 'react'
import {useParams } from "react-router-dom";
import {CardActionArea, CardActions } from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import {Button, Box, Paper, Grid, Typography, CssBaseline, ThemeProvider} from '@mui/material';
import Container from '@mui/material/Container'

function ActionOptions({action, user}) {
  console.log(user)
  console.log(action.id)

  /*------------------STATE--------------------*/
  //4.action state
  const [selectAction, setSelectAction] = useState(true)

  //5. prompt state
  const [prompt, setPrompt] = useState([])

  /*------------------STATE--------------------*/
  /*-------------------CRUD--------------------*/
  
  useEffect(() => {
      fetch(`/api/jprompts/${action.id}`)
      .then(res => res.json())
      .then(prompt => {
          setPrompt(prompt)
      })
  },[])


  // const addAsCompleted = (journal_prompt_id, nudge_prompt_id, user_id) => {
  //   fetch("/api/completed/add", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify({
  //       user_id: user_id,
  //       journal_prompt_id: journal_prompt_id,
  //       nudge_prompt_id: nudge_prompt_id,
  //     }),
  //   })
  //     .then((response) => response.json())
  //     .then((data) => {
  //       console.log("Added to completed prompts", data);
  //     })
  //     .catch((error) => {
  //       console.error("Couldn't add to completed prompts", error);
  //     });
  // };
  

  // console.log(user.id)
  // console.log(id)
  // function handlePrompts(e, id){
  //   fetch(`/api/completed_prompt`, {
  //     method: 'POST',
  //     headers: {
  //       "content-type":"application/json"
  //     },
  //     body: JSON.stringify({
  //       journal_prompt_id: id,
  //       user_id: user.id
  //     }),
  //   })
    
  //   .then(res => res.json())
  //   .then(data => console.log(data))
  // }
  /*-------------------CRUD--------------------*/
  /*------------------CONST--------------------*/

  let prompt_arr = Object.values(prompt)
 
  const ipickyou = prompt_arr[Math.floor(Math.random() * prompt_arr.length)]
  console.log(ipickyou)

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
          {/* <Button onClick={(e) => handlePrompts(e, id)}>Completed!</Button> */}
      </CardContent>
      
  </Card>
  )}
  </div>
)
}

export default ActionOptions
  