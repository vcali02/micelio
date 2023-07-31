import React from 'react'
import Growth from './Growth'

function GrowthContainer({compPrompt}) {
    console.log(compPrompt)
    const mapped_prompts = [...compPrompt].map(el => (
     <Grid item xs={3}>
        <Growth key={el.id} prompt={el}/>
       </Grid>
    ))
    console.log(mapped_prompts)
   
     return (
         <>
           <Grid container>
             {mapped_prompts}
           </Grid>
          
         </>
           
         
     )
   }

export default GrowthContainer