import React from 'react'
import Recommended from "./Recommended"
import {Grid} from '@mui/material';

function RecContainer({recs}) {

const rec = [...recs].map(el => (
  <Grid item xs={6}>
    <Recommended key={el.id} rec={el}/>
  </Grid>
))


  return (
    <div >
        {/*1. map through each recommendation*/}
      
        <Grid  container spacing={{ xs: 1, md: 2 }} >
          {rec}
        </Grid>

    </div>
  )
}

export default RecContainer