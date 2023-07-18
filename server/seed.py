#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, CompletedPrompt, NudgePrompt, Nudge, JournalPrompt, Journal, Pillar, Recommendation

#instantiating faker
fake = Faker()

###NUDGE AND JOURNAL PROMPTS WITH NULL
#how to separate prompts per pillar
#journal prompt has journal id which goes to pillars 
#journal prompts has pillars through journals 

if __name__ == '__main__':
    #a context (the state of the environment where the code is being executed) through which Flask and its extensions are accessible
    with app.app_context():
        print("Clearing database...")
        User.query.delete()
        NudgePrompt.query.delete()
        JournalPrompt.query.delete()
        Nudge.query.delete()
        Journal.query.delete()
        CompletedPrompt.query.delete()
        Recommendation.query.delete()
        Pillar.query.delete()

        db.session.commit()
    
        #---------------USERS---------------#
        print("Seeding users...")
        user_images = [
            "https://static.wixstatic.com/media/7fa9fc_b8ab50165aef4381894173e6b9b61cf7~mv2.jpg/v1/fit/w_241,h_362,q_90/7fa9fc_b8ab50165aef4381894173e6b9b61cf7~mv2.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGyke_NFD7rJOPbpWMXcToWw3l-7x1Vpdaq4cSZg-b-gnQOFbFTBJ9Cn2Bg4fzY48RP18&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXURdXvXDNRGwlQjRXcJFgqVuxVKKtw3w4XQ&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCio6ILKi4nvLmBv7gQz7cHiKxi81WLSvAzpvfsQqqI6lDOeJBVjhK-06sKANwta-AjUw&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3YjghHLn-nKcAx2uggKa0hrWBMxdkifx5kLkAZsNaG4bOW87vD3KZiCrzcdJ-dlf1AVE&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRreaDq9iNCgzN_ppzywb0fKwc9ZEyE2xnpsg&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnPx6e5PsPM7PX4RQHbAzLftgME0teV38unw&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7iWoaZ8ndCK8VLnr-6H7LtKFIU1QvW-XNtA&usqp=CAU",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd8gBjf2qnfd4SClmjDKo8xPnZwOjYUHAcZw&usqp=CAU",
            "https://i.pinimg.com/originals/c8/1a/8b/c81a8b6bcee899a76686672e8832863e.jpg"
        ]

        users = []
        for i in range(10):
            user_image = rc(user_images)
            users.append(User(name= fake.name(), email= fake.email(), username= fake.user_name(), image= user_image, bio= fake.sentence(10)))
        
        db.session.add_all(users)
        #---------------USERS---------------#





        #-----------NUDGE PROMPTS-----------#
        #PILLAR 1 be impeccable with your word
        print("Seeding pillar one nudge action prompts...")
        p1n_action_prompts = [
            "Correct negative self talk. ex: `I can't do this.` to `This is hard, but I'm still learning.`",
            "Ask yourself: Is what I'm saying helping me achieve my goal?",
            "Do one thing that makes you feel cared for today.",
            "Today's mantra: When I love myself, I express love.",
            "Ask yourself: Do I agree with the opinion that was shared with me?",
            "Ask yourself: Will gossip fuel me or hinder me?",
            "Don't let your mind be fertile ground for negativity.",
            "Do one thing to make someone feel cared for today.",
            "Words are magic, find a way to use them to change someone's day for the better.",
            "Consider the impact of others' words on your mindset and offer someone a genuine compliment."
        ]
        
        #PILLAR 1 be impeccable with your word
        print("Seeding pillar one nudge prompts...")
        p1_nudge_prompts = []
        for i in range(10):
            one_p1_prompt = rc(p1n_action_prompts)
            p1_nudge_prompts.append(
                NudgePrompt(action_prompt=one_p1_prompt, nudges_id=1)
            )
        db.session.add_all(p1_nudge_prompts)

        #PILLAR 2 don't take anything personally 
        print("Seeding pillar two nudge action prompts...")
        p2n_action_prompts = [
            "When someone's words or actions leave you unsteady, ask them: Tell me how you decided that was an okay thing to say/do?",
            "Reminder: The behavior of others cannot rule you without first giving it permission to do so.",
            "Reminder: You are no more a one eyed, one horned, flying purple people eater, than you are whatever anyone says you are.",
            "When someone's words or actions leave you unsteady, ask yourself: What must this person be dealing with that they cannot act with kindness?",
            "When someone's words or actions leave you unsteady, consider the wounds you have that have been touched by what has been said.",
            "When someone sends you emotional poison, decide if you'd like to eat it.",
            "Remind a friend that they too, can choose to deny the poison of others.",
            "Remind someone that they are allowed to change their mind.",
            "Tell a friend in distress the power of unsubscribing to other's poison."
            "Lend an ear to someone in need."
        ]

        #PILLAR 2 don't take anything personally
        print("Seeding pillar two nudge prompts...")
        p2_nudge_prompts = []
        for i in range(10):
            one_p2_prompt = rc(p2n_action_prompts)
            p2_nudge_prompts.append(
                NudgePrompt(action_prompt=one_p2_prompt, nudges_id=2)
            )
        db.session.add_all(p2_nudge_prompts)

        #PILLAR 3 don't make assumptions
        print("Seeding pillar three nudge action prompts...")
        p3n_action_prompts = [
            "Communication gives you the power to gain knowledge. Ask questions to better understand someone's perspective.",
            "While we cannot control others, we can control ourselves. Take a pause before responding to conflict.",
            "Communicate your needs in your personal relationships. People can't read your mind.",
            "Communicate your needs in your professional relationships. People can't read your mind.",
            "Ask someone what they need from you. You cannot read minds.",
            "Ask yourself how you allow an assumption to ring true, even when it's not, simply to avoid being wrong.",
            "Have courage, ask questions.",
            "Pick a person, and see the world through their eyes today.",
            "Encourage someone to abandon their fear of being themselves by celebrating who they are today.",
            "Find ways to accept people without wanting to change them."
        ]

        #PILLAR 3 don't make assumptions
        print("Seeding pillar three nudge prompts...")
        p3_nudge_prompts = []
        for i in range(10):
            one_p3_prompt = rc(p3n_action_prompts)
            p3_nudge_prompts.append(
                NudgePrompt(action_prompt=one_p3_prompt, nudges_id=3)
            )
        db.session.add_all(p3_nudge_prompts)

        #PILLAR 4 always do your best 
        print("Seeding pillar four nudge action prompts...")
        p4n_action_prompts = [
            "Check in with yourself: Did you do the best you could given your current state?",
            "Consider how the state of `success` ebbs and flows based on the available resources of your current state.",
            "Encourage someone to view the value of their efforts higher than the value of the current outcome.",
            "Where can you give yourself grace today and congratulate yourself for the growth you have done?"
            "Where can you give someone grace today and accept someone for where they are?",
            "Your best is never going to be the same from one moment to the next. How can you use this to empower you?",
            "Does thinking 'I could have done better' help you accomplish your goals?",
            "Take action for the sake of it, and don't expect a reward.",
            "When you don't do your best, you deny yourself the right to be you.",
            "Shift your perspective on what is 'your best' and you will find yourself more at peace with your growth."
        ]

        #PILLAR 4 always do your best 
        print("Seeding pillar four nudge prompts...")
        p4_nudge_prompts = []
        for i in range(10):
            one_p4_prompt = rc(p4n_action_prompts)
            p4_nudge_prompts.append(
                NudgePrompt(action_prompt=one_p4_prompt, nudges_id=4)
            )
        db.session.add_all(p4_nudge_prompts)

        #-----------NUDGE PROMPTS-----------#





        #----------JOURNAL PROMPTS----------#
        #PILLAR 1 be impeccable with your word
        print("Seeding pillar one journal action prompts...")
        p1j_action_prompts = [
            "Journal about the grand destruction and magnificence that is created through speech.",
            "Journal about this concept: How much you love yourself and how you feel about yourself are directly proportionate to the quality and integrity of your word.",
            "Journal about the misuse of your word as poison for both yourself and the person you use it against.",
            "Journal about the imprint people's opinions have on others.",
            "Journal about what living through love looks like to you.",
            "Journal about this concept: A sin is anything that you do which goes against yourself. Everything you feel or believe or say that goes against yourself is a sin.",
            "Journal about manifesting your reality through your word, impeccable or otherwise.",
            "Journal about a time your point of view was not `true` but simply your point of view.",
            "Journal about how you use your words to speak to yourself and what, if anything, might you change to uplift the relationship you have with yourself.",
            "Journal about this concept: You will only receive a negative idea if your mind is fertile ground for that idea."
        ]
        
        #PILLAR 1 be impeccable with your word
        print("Seeding pillar one journal prompts...")
        p1_journal_prompts = []
        for i in range(10):
            one_p1_prompt = rc(p1j_action_prompts)
            p1_journal_prompts.append(
                JournalPrompt(action_prompt=one_p1_prompt, journals_id=1)
            )
        db.session.add_all(p1_journal_prompts)

        #PILLAR 2 don't take anything personally
        print("Seeding pillar two journal action prompts...")
        p2j_action_prompts = [
            "Journal about this concept: You take things personally because a part of you agrees with whatever was said. As soon as you agree, the poison goes through you.",
            "Journal about this concept: People spew poison at others because they are dealing with their own feelings, beliefs, and opinions, and unable to love accept themselves enough to accept others.",
            "Journal about a time you took something personally and unravel it by applying the concept that it was never about you.",
            "Journal about the idea that you love others best when you love yourself first.",
            "Journal about how deciding to deny the emotional poison someone sends you becoming worse to the sender but not to you.",
            "Journal about this concept: If you do not take things personally, you are immune to the poison.",
            "Journal about a time when the agreements in your mind were not compatible, which agreement you chose to listen to, and how it made you feel.",
            "Journal about the difference between understanding someone's trauma and subjecting yourself to gaslighting.",
            "Journal about where in your life you can apply the concept that you are not responsible for the actions of others and only responsible for yourself. ",
            "Journal about how your world and your life is simply a movie of your perception of existence."
        ]
        
        #PILLAR 2 don't take anything personally
        print("Seeding pillar two journal prompts...")
        p2_journal_prompts = []
        for i in range(10):
            one_p2_prompt = rc(p2j_action_prompts)
            p2_journal_prompts.append(
                JournalPrompt(action_prompt=one_p2_prompt, journals_id=2)
            )
        db.session.add_all(p2_journal_prompts)

        #PILLAR 3 don't make assumptions
        print("Seeding pillar three journal action prompts...")
        p3j_action_prompts = [
            "Journal about a time an assumption was made, there were misunderstandings, things were taken personally, and drama ensued for nothing.",
            "Journal about this concept: Because we are afraid to ask for clarification, we make assumptions, and believe we are right about the assumptions.",
            "Journal about a time when you made an assumption when you didn't understand something, and when the truth came out, the bubble of your assumption popped and what you found out was not what you thought at all.",
            "Journal about a time when you made an assumption and stuck to it, not because it was correct, but because it made you feel safe.",
            "Journal about the idea that we fear being ourselves around others because we thing everyone will judge , victimize, abuse, and blame us as we do ourselves.",
            "Journal about a time you rejected yourself before anyone else had a chance to.",
            "Journal about a time your over or underestimated yourself because you didn't take the time to ask yourself questions and answer them.",
            "Journal about how human problems can be solved through clear communication.",
            "Journal about the courage it takes to ask questions.",
            "Journal about a time you found your voice and used it to get something you wanted. How did it benefit you and how can you apply this in other areas of your life?"
        ]
        
        #PILLAR 3 don't make assumptions
        print("Seeding pillar three journal prompts...")
        p3_journal_prompts = []
        for i in range(10):
            one_p3_prompt = rc(p3j_action_prompts)
            p3_journal_prompts.append(
                JournalPrompt(action_prompt=one_p3_prompt, journals_id=3)
            )
        db.session.add_all(p3_journal_prompts)


        #PILLAR 4 always do your best
        print("Seeding pillar four journal action prompts...")
        p4j_action_prompts = [
            "Journal about the ebb and flow of `your best,` as you keep in mind that your best is never the same from one moment to the next.",
            "Journal about a time you dishonored your present `best` by pushing yourself beyond your present limits and the burnout it likely led you to.",
            "Journal about a time you dishonored your present `best` by not pushing yourself to meet your present potential and the guilt or shame it may have led to.",
            "Journal about how honoring `your best` can allow you to give yourself grace, and celebrate your successes.",
            "Journal about the idea that you do not exist to sacrifice joy or your life. You are here to live and experience happiness and love.",
            "Journal about this concept: When you do your best you learn to accept yourself.",
            "Journal about the difference between taking action out of pure desire and without the need for reward, and taking action because you have to.",
            "Journal about how letting go of the past allows you to enjoy the life you are experiencing now.",
            "Journal about this concept: When you don't do your best, you deny yourself the right to be you.",
            "Journal about a time you got knocked down and got back up again. Elaborate and consider how that commitment can be applied to other areas of your life."
        ]
        
        #PILLAR 4 always do your best
        print("Seeding pillar four journal prompts...")
        p4_journal_prompts = []
        for i in range(10):
            one_p4_prompt = rc(p4j_action_prompts)
            p4_journal_prompts.append(
                JournalPrompt(action_prompt=one_p4_prompt, journals_id=4)
            )
        db.session.add_all(p4_journal_prompts)

        #----------JOURNAL PROMPTS----------#





        #--------------NUDGES---------------#
        print("Seeding nudges...")
      
        p1_nudges = [
            Nudge(image="https://assets.artfullywalls.com/works/40944/big-thumb-2022-03-03-ASX_FrfMjM0Vppm8x9nCJC8fffXbJlgU7D89bpyItFC8BVBd6UT-7UpBOwQ2dV-e-oFvhDQGZsc-E1wL.jpg", action_type="nudge", description="A nudge is a thought exercise to challenge you to push your comfort zone and apply the pillars of growth to yourself and those around you.", pillar_id=1)
        ]
        db.session.add_all(p1_nudges)

        p2_nudges = [
            Nudge(image="https://assets.artfullywalls.com/works/40944/big-thumb-2022-03-03-ASX_FrfMjM0Vppm8x9nCJC8fffXbJlgU7D89bpyItFC8BVBd6UT-7UpBOwQ2dV-e-oFvhDQGZsc-E1wL.jpg", action_type="nudge", description="A nudge is a thought exercise to challenge you to push your comfort zone and apply the pillars of growth to yourself and those around you.", pillar_id=2)
        ]
        db.session.add_all(p2_nudges)

        p3_nudges = [
            Nudge(image="https://assets.artfullywalls.com/works/40944/big-thumb-2022-03-03-ASX_FrfMjM0Vppm8x9nCJC8fffXbJlgU7D89bpyItFC8BVBd6UT-7UpBOwQ2dV-e-oFvhDQGZsc-E1wL.jpg", action_type="nudge", description="A nudge is a thought exercise to challenge you to push your comfort zone and apply the pillars of growth to yourself and those around you.", pillar_id=3)
        ]
        db.session.add_all(p3_nudges)

        p4_nudges = [
            Nudge(image="https://assets.artfullywalls.com/works/40944/big-thumb-2022-03-03-ASX_FrfMjM0Vppm8x9nCJC8fffXbJlgU7D89bpyItFC8BVBd6UT-7UpBOwQ2dV-e-oFvhDQGZsc-E1wL.jpg", action_type="nudge", description="A nudge is a thought exercise to challenge you to push your comfort zone and apply the pillars of growth to yourself and those around you.", pillar_id=4)
        ]
        db.session.add_all(p4_nudges)


        #--------------NUDGES---------------#





        #-------------JOURNALS--------------#
        print("Seeding journals...")
        p1_journals = [
            Journal(image="https://d3ui957tjb5bqd.cloudfront.net/uploads/images/5/57/57856.twitter.jpg?fmt=webp&1623045360", action_type="journal", description="Journaling offers two critical components to personal growth. The first, it uses your subconscious mind to develop and process your thoughts on a topic. Second, it allows a point of reference when looking back at your writing to both see how much you have grown, and what your stream of thought is capable of developing. ", pillar_id=1)
        ]
        db.session.add_all(p1_journals)

        p2_journals = [
            Journal(image="https://d3ui957tjb5bqd.cloudfront.net/uploads/images/5/57/57856.twitter.jpg?fmt=webp&1623045360", action_type="journal", description="Journaling offers two critical components to personal growth. The first, it uses your subconscious mind to develop and process your thoughts on a topic. Second, it allows a point of reference when looking back at your writing to both see how much you have grown, and what your stream of thought is capable of developing. ", pillar_id=2)
        ]
        db.session.add_all(p2_journals)

        p3_journals = [
            Journal(image="https://d3ui957tjb5bqd.cloudfront.net/uploads/images/5/57/57856.twitter.jpg?fmt=webp&1623045360", action_type="journal", description="Journaling offers two critical components to personal growth. The first, it uses your subconscious mind to develop and process your thoughts on a topic. Second, it allows a point of reference when looking back at your writing to both see how much you have grown, and what your stream of thought is capable of developing. ", pillar_id=3)
        ]
        db.session.add_all(p3_journals)

        p4_journals = [
            Journal(image="https://d3ui957tjb5bqd.cloudfront.net/uploads/images/5/57/57856.twitter.jpg?fmt=webp&1623045360", action_type="journal", description="Journaling offers two critical components to personal growth. The first, it uses your subconscious mind to develop and process your thoughts on a topic. Second, it allows a point of reference when looking back at your writing to both see how much you have grown, and what your stream of thought is capable of developing. ", pillar_id=4)
        ]
        db.session.add_all(p4_journals)
        #-------------JOURNALS--------------#




        # fencers https://c8.alamy.com/comp/2FA1X8C/contemporary-art-collage-modern-design-summer-mood-two-fencing-girls-using-flowers-for-fighting-on-white-2FA1X8C.jpg
        #teal eye hands https://as1.ftcdn.net/v2/jpg/04/30/75/34/1000_F_430753455_X6NC8wh96BleXVBiBQiSAT2M64K8xfBK.jpg
        # green people 2nd pillar https://www.shutterstock.com/image-photo/group-people-family-flower-bud-260nw-2281726391.jpg
        #pillar 4 reading https://d3ui957tjb5bqd.cloudfront.net/uploads/images/5/57/57856.twitter.jpg?fmt=webp&1623045360
        #--------------PILLARS--------------#
        print("Seeding pillars...")
        pillars = [
            Pillar(image="https://images.squarespace-cdn.com/content/v1/5e69d2c66d9167038ff7d12c/1632982781392-AIT7XGWVWSS0DQQERKZN/IMG_6325.jpg", pillar_name="Be impeccable with your word.", description="With just the power of your word you can create the most beautiful of dreams, or destroy everything around you."),
            Pillar(image="https://cdn.domestika.org/c_limit,dpr_auto,f_auto,q_auto,w_820/v1556809760/content-items/002/963/681/surrealism-3-original.jpg?1556809760", pillar_name="Don't take anything personally.", description="Nothing other people do is because of you. It is because of themselves."),
            Pillar(image="https://media.istockphoto.com/id/1201257225/vector/hands-raised-with-eyes-on-palms-watching-mysterious-and-spiritual-horizontal-design.jpg?s=612x612&w=0&k=20&c=gEZWDWCVZHEdWFXGKrmjVy5IS39WLz19bxem5pja-RI=", pillar_name="Don't make assumptions.", description="You cannot assume that everyone sees the world the way you do."),
            Pillar(image="https://d7hftxdivxxvm.cloudfront.net/?height=800&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2FQafdH8KJYqyyDDV4i4WBpQ%2Fnormalized.jpg&width=666", pillar_name="Always do your best.", description="If you always do your best there is no way you can judge yourself.")
        ]
        db.session.add_all(pillars)
        #--------------PILLARS--------------#





        #---------COMPLETED PROMPTS---------#
        #PILLAR 1 be impeccable with your word
        print("Seeding pillar one completed prompts...")
        p1_completed_prompts = []
        for i in range(20):
            one_user = rc(users)
            nudge_prompt = rc(p1_nudge_prompts)
            journal_prompt = rc(p1_journal_prompts)
            p1_completed_prompts.append(
                CompletedPrompt(user_id=one_user.id, user=one_user, nudge_prompt_id=nudge_prompt.id, nudge_prompt=nudge_prompt, journal_prompt_id=journal_prompt.id, journal_prompt=journal_prompt)
            )
        db.session.add_all(p1_completed_prompts)
        
        #PILLAR 2 don't take anything personally
        print("Seeding pillar two completed prompts...")
        p2_completed_prompts = []
        for i in range(20):
            one_user = rc(users)
            nudge_prompt = rc(p2_nudge_prompts)
            journal_prompt = rc(p2_journal_prompts)
            p2_completed_prompts.append(
                CompletedPrompt(user_id=one_user.id, user=one_user, nudge_prompt_id=nudge_prompt.id, nudge_prompt=nudge_prompt, journal_prompt_id=journal_prompt.id, journal_prompt=journal_prompt)
            )
    
        db.session.add_all(p2_completed_prompts)

        #PILLAR 3 don't make assumptions
        print("Seeding pillar three completed prompts...")
        p3_completed_prompts = []
        for i in range(20):
            one_user = rc(users)
            nudge_prompt = rc(p3_nudge_prompts)
            journal_prompt = rc(p3_journal_prompts)
            p3_completed_prompts.append(
                CompletedPrompt(user_id=one_user.id, user=one_user, nudge_prompt_id=nudge_prompt.id, nudge_prompt=nudge_prompt, journal_prompt_id=journal_prompt.id, journal_prompt=journal_prompt)
            )
        db.session.add_all(p3_completed_prompts)

        #PILLAR 4 always do your best
        print("Seeding pillar four completed prompts...")
        p4_completed_prompts = []
        for i in range(20):
            one_user = rc(users)
            nudge_prompt = rc(p4_nudge_prompts)
            journal_prompt = rc(p4_journal_prompts)
            p4_completed_prompts.append(
                CompletedPrompt(user_id=one_user.id, user=one_user, nudge_prompt_id=nudge_prompt.id, nudge_prompt=nudge_prompt, journal_prompt_id=journal_prompt.id, journal_prompt=journal_prompt)
            )
        db.session.add_all(p4_completed_prompts)
        
        #---------COMPLETED PROMPTS---------#





        #----------RECOMMENDATIONS----------#
        print("seeding recommendations...")
        recommendations = [
            Recommendation(rec_type="Book: The Four Agreements", 
            rec_link = "https://www.amazon.com/Four-Agreements-Practical-Personal-Freedom/dp/1878424319/ref=sr_1_1?crid=VN873KBQI7U&keywords=the+four+agreements&qid=1689004212&sprefix=the+four+agreement%2Caps%2C155&sr=8-1", 
            image="https://m.media-amazon.com/images/I/81hHy5XrdKL._SL1330_.jpg", 
            blurb="This tiny yet powerful book is the groundwork for growth whether you are building, rebuilding, adding, or remodelling your self."),
            Recommendation(rec_type="Podcast: The Huberman Lab", 
            rec_link = "https://open.spotify.com/show/79CkJF3UJTHFV8Dse3Oy0P?si=5018200337e0465c", 
            image="https://i.scdn.co/image/ab6765630000ba8aaa4830256e4b613f07287208", 
            blurb="Andrew Huberman uses his expertise in neurobiology and ophthalmology to share science based tools to support people's everyday life. Exploring any episode of his is a life-changing experience.")
        ]
        db.session.add_all(recommendations)
        #----------RECOMMENDATIONS----------#


        db.session.commit()
        print("Done seeding!")
        # Seed code goes here!
  
