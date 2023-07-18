import React, {useState} from 'react'
import {Drawer, IconButton, List, ListItemButton, ListItemIcon, ListItemText} from '@mui/material'
import ListIcon from '@mui/icons-material/List';

function DrawerComp({micelio, about, pillars, methods, growth, recommended}) {
/*------------------STATE--------------------*/

    const [open, setOpen] = useState(false)


  return (
    <div>
        <Drawer PaperProps={{
            sx:{backgroundColor: "#E8A78B"},
        }}
            open={open} onClose={() => setOpen(false)}>
        <List>
            <ListItemButton divider onClick={()=>setOpen(false)}>
                <ListItemIcon>
                    <ListItemText>{micelio}</ListItemText>
                </ListItemIcon>
            </ListItemButton>
            <ListItemButton divider onClick={()=>setOpen(false)}>
                <ListItemIcon>
                    <ListItemText>{about}</ListItemText>
                </ListItemIcon>
            </ListItemButton>
            <ListItemButton divider onClick={()=>setOpen(false)}>
                <ListItemIcon>
                    <ListItemText>{pillars}</ListItemText>
                </ListItemIcon>
            </ListItemButton>
            <ListItemButton divider onClick={()=>setOpen(false)}>
                <ListItemIcon>
                    <ListItemText>{methods}</ListItemText>
                </ListItemIcon>
            </ListItemButton>
            <ListItemButton divider onClick={()=>setOpen(false)}>
                <ListItemIcon>
                    <ListItemText>{growth}</ListItemText>
                </ListItemIcon>
            </ListItemButton>
            <ListItemButton divider onClick={()=>setOpen(false)}>
                <ListItemIcon>
                    <ListItemText>{recommended}</ListItemText>
                </ListItemIcon>
            </ListItemButton>
        </List>
        </Drawer>
        <IconButton sx={{marginTop: "150px", marginLeft: "auto"}} onClick={()=>setOpen(!open)}>
            <ListIcon/>
        </IconButton>
    </div>
  )
}

export default DrawerComp