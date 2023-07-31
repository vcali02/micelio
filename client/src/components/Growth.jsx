import React, {useContext, useState, useEffect} from 'react'
import Context from "./Context"

function Growth({prompt}) {
  console.log(trail.id)

  function deleteCompPrompt(){
   fetch(`api/completed_prompt/${trail.id}`, {
     method: 'DELETE'
   })
 }
 
 
   return (
   
     <Container className= "card-margin-top">
     <Card sx={{ minWidth: 345, maxHeight: 425 }}>
       <CardActionArea>
       {/* <CardMedia
           component="img"
           height="140"
           image={prompt.journal_prompt_id}
           alt={prompt.journal_prompt_id}
         /> */}
       <CardContent>
       
         <Typography>{prompt.journal_prompt_id}</Typography>
         <Typography>{prompt.journal_prompt_id}</Typography>
         <Button>Edit</Button>
         <Button onClick={(e) => deleteCompPrompt(e)}>Remove</Button>
       </CardContent>
       </CardActionArea>
     </Card>
     </Container>
   )
 }

export default Growth