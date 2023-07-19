# micelio - expand your hidden dimensions 

## As a user you can:
- explore the four pillars of expansion
- explore methods for expansion
- view your growth
- navigate home
- explore recommended stimuli
- learn about micelio
- log in and out


## Wireframe
https://www.figma.com/file/hRXCinhvPWBrCFlWpTpQmO/micelio?type=design&node-id=0-1&mode=design&t=AYhDihunhCv6L994-0
![Screenshot 2023-07-04 at 3 27 56 PM](https://github.com/vcali02/micelio/assets/122405969/1f25688d-f7fa-4745-8d3d-9aaef76b49cb)
![Screenshot 2023-07-04 at 3 28 53 PM](https://github.com/vcali02/micelio/assets/122405969/ee550e44-a30d-44bd-a4c1-fda31c7adf8b)
![Screenshot 2023-07-04 at 3 28 20 PM](https://github.com/vcali02/micelio/assets/122405969/c953bf56-09bb-4565-aacf-de9632cf7cb1)
![Screenshot 2023-07-04 at 3 29 02 PM](https://github.com/vcali02/micelio/assets/122405969/7f5e9a86-bab5-4cd2-848d-19cbf4df4b89)

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
![Screenshot 2023-07-05 at 10 05 35 AM](https://github.com/vcali02/micelio/assets/122405969/46e89ac4-d904-4fdd-bde4-2475aa0f5d2c)




## Client-side Routes
| Client Route   | Component     |
|----------------|---------------|
| /home              | Home.js        |
| /about        | About.js  |
| /pillars      | Pillars.js  |
| /methods | Journal.js and Nudge.js|
| /signup    | Auth.js  |
| //login    | Auth.js  |
| /recommended        | Recommended.js     |
| /growth         | CompletedPrompts.js  |


