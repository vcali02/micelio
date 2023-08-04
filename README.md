# micelio - expand your hidden dimensions 

## As a user you can:
- explore the four pillars of expansion
- explore methods for expansion
- navigate home
- explore recommended stimuli
- learn about micelio
- create an account, log in and out


## Wireframe
https://www.figma.com/file/hRXCinhvPWBrCFlWpTpQmO/micelio?type=design&node-id=0-1&mode=design&t=AYhDihunhCv6L994-0
![Screenshot 2023-07-19 at 3 19 44 PM](https://github.com/vcali02/micelio/assets/122405969/c81da462-1cb3-4969-9054-b56d2a8ed316)
![Screenshot 2023-07-19 at 3 19 58 PM](https://github.com/vcali02/micelio/assets/122405969/783c6ca3-f3f3-4419-926f-c5511510bba7)
![Screenshot 2023-07-19 at 3 20 11 PM](https://github.com/vcali02/micelio/assets/122405969/be7e08b5-a4e5-4fa0-bf17-8ef6cc665f09)
![Screenshot 2023-07-19 at 3 20 24 PM](https://github.com/vcali02/micelio/assets/122405969/0a81c596-9266-4d4b-8a51-c4bf45e94ff4)
![Screenshot 2023-07-19 at 3 20 48 PM](https://github.com/vcali02/micelio/assets/122405969/d77fb1af-5cac-43a1-8903-66edc1bd1ee1)
![Screenshot 2023-07-19 at 3 21 16 PM](https://github.com/vcali02/micelio/assets/122405969/83d848a5-0894-4dc5-a389-8f1483204130)
![Screenshot 2023-07-19 at 3 21 30 PM](https://github.com/vcali02/micelio/assets/122405969/efd39b75-d14d-4d86-a29a-c404dda48259)
![Screenshot 2023-07-19 at 3 21 49 PM](https://github.com/vcali02/micelio/assets/122405969/8553872a-9b28-4d59-bfbe-1b15ed3e5e7c)


## Schema
![Screenshot 2023-07-04 at 3 29 51 PM](https://github.com/vcali02/micelio/assets/122405969/cf779568-94f3-476f-9960-d3765034664d)

### Relationships
- one user has many completed prompts; many prompts are completed by one user
- one user has completed nudges through completed prompts
- ^the same for completed journals

- one nudge prompt has many completed prompts; many completed prompts are a nudge prompt
- ^the same for journal

- one nudge has many prompts; many nudge prompts belong to one nudge
- ^ the same for journal

- one pillar has one nudge; one nudge has one pillar
- ^the same for journal


## API Routes
| API Route                | Method | Response                                                                                                                                                          |
|--------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /user             | GET    | user display                                                 |
| /user             | POST   |  user display                                                                           |
| /user/<int:id>    | GET    | user display                                                              |
| /user/<int:id>    | PATCH  | user display                                                      |
| /user/<int:id>    | DELETE |  {}                                                                                                                                                                |
| /completed_prompts      | GET    | completed prompts display |
| /completed_prompts/<int:id> | GET    | completed prompts display         |
| /completed_prompts       | POST   |  completed prompts display                                                                           |
| /completed_prompts/<int:id> | DELETE |  {}                                                                                                                                                                |
| /nudge_prompt            | GET    | nudge prompt display                                                     |
| /nudge_prompt/<int:id>   | GET    | nudge prompt display                                                                              |
| /nudge_prompt       | POST   | nudge prompt display                                                                              |
| /nudge_prompt/<int:id>   | DELETE | {}                                                                                                                                                                |
| /journal_prompt            | GET    | journal prompt display                                                             |
| /journal_prompt/<int:id>   | GET    | journal prompt display                                                                          |
| /journal_prompt       | POST   |  journal prompt display                                                                         |
| /journal_prompt/<int:id>   | DELETE |  {}                                                                                                                                                              |
| /nudge           | GET    |   nudge display                                                                           |
| /journal           | GET    | journal display                                                                          |
| /pillar           | GET    |   pillar display                                          |
| /pillar/<int:id> | GET    |  pillar display            |
| /recommended      | GET    |   recommended display  |
| /recommended/<int:id> | GET    |  recommended display          |
| /recommended       | POST   |  recommended display                                                                         |
| /recommended/<int:id> | DELETE |  {}                                                                                                                                                                |
|/login | POST | success and authorized|  |
|/logout | DELETE | {} |

## React Component Tree
![Screenshot 2023-07-19 at 3 18 15 PM](https://github.com/vcali02/micelio/assets/122405969/18b98f14-4585-404e-9161-4420b4000945)




## Client-side Routes
| Client Route   | Component     |
|----------------|---------------|
| /home              | Home.jsx        |
| /about        | About.jsx  |
| /pillars      | Pillars.jsx  |
| /methods/pillars_id | ActionContainer.jsx|
| /signup    | Auth.jsx  |
| //login    | Auth.jsx  |
| /recommended        | Recommended.jsx     |
| /growth         | CompletedPrompts.js  |


## Instructions
Open two terminals and input commands below:
```
#for backend
$ cd server
$ pipenv install
$ pipenv shell
```

```
# for frontend
$ cd client
$ npm install
$ npm run dev
```


