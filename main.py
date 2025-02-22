from flask import Flask,request
import random
import os 
app = Flask(__name__)

# List of 200+ Bible verses
bible_verse = [
    {
        "quote": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
        "emotion": "love",
        "author": "John",
        "book": "John",
        "reference": "John 3:16"
    },
    {
        "quote": "The Lord is my shepherd; I shall not want.",
        "emotion": "peace",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:1"
    },
    {
        "quote": "I can do all this through him who gives me strength.",
        "emotion": "strength",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:13"
    },
    {
        "quote": "The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
        "emotion": "comfort",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:18"
    },
    {
        "quote": "For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you a hope and a future.",
        "emotion": "hope",
        "author": "Jeremiah",
        "book": "Jeremiah",
        "reference": "Jeremiah 29:11"
    },
    {
        "quote": "The Lord is my light and my salvation— whom shall I fear? The Lord is the stronghold of my life— of whom shall I be afraid?",
        "emotion": "courage",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 27:1"
    },
    {
        "quote": "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control.",
        "emotion": "fruit of the Spirit",
        "author": "Paul",
        "book": "Galatians",
        "reference": "Galatians 5:22-23"
    },
    {
        "quote": "The Lord is my refuge and fortress, my God, in whom I trust.",
        "emotion": "trust",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 91:2"
    },
    {
        "quote": "Cast your cares on the Lord and he will sustain you; he will never let the righteous be shaken.",
        "emotion": "reliance",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 55:22"
    },
    {
        "quote": "For nothing is impossible with God.",
        "emotion": "faith",
        "author": "Luke",
        "book": "Luke",
        "reference": "Luke 1:37"
    },
    {
        "quote": "The Lord will fight for you; you need only to be still.",
        "emotion": "peace",
        "author": "Moses",
        "book": "Exodus",
        "reference": "Exodus 14:14"
    },
    {
        "quote": "Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.",
        "emotion": "assurance",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 41:10"
    },
    {
        "quote": "I will never leave you nor forsake you.",
        "emotion": "comfort",
        "author": "God",
        "book": "Hebrews",
        "reference": "Hebrews 13:5"
    },
    {
        "quote": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
        "emotion": "hope",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:28"
    },
    {
        "quote": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
        "emotion": "peace",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:6"
    },
    {
        "quote": "The Lord is gracious and compassionate, slow to anger and rich in love.",
        "emotion": "grace",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:8"
    },
    {
        "quote": "For the mountains may depart and the hills be removed, but my steadfast love shall not depart from you, and my covenant of peace shall not be removed,” says the Lord, who has compassion on you.",
        "emotion": "steadfast love",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 54:10"
    },
    {
        "quote": "Do not let your hearts be troubled. You believe in God; believe also in me.",
        "emotion": "comfort",
        "author": "Jesus",
        "book": "John",
        "reference": "John 14:1"
    },
    {
        "quote": "And we have the word of the prophets made more certain, and you will do well to pay attention to it, as to a light shining in a dark place, until the day dawns and the morning star rises in your hearts.",
        "emotion": "guidance",
        "author": "Peter",
        "book": "2 Peter",
        "reference": "2 Peter 1:19"
    },
    {
        "quote": "He heals the brokenhearted and binds up their wounds.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 147:3"
    },
    {
        "quote": "For the Lord gives wisdom; from his mouth come knowledge and understanding.",
        "emotion": "wisdom",
        "author": "Solomon",
        "book": "Proverbs",
        "reference": "Proverbs 2:6"
    },
    {
        "quote": "The Lord is near to all who call on him, to all who call on him in truth.",
        "emotion": "closeness",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:18"
    },
    {
        "quote": "Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here!",
        "emotion": "renewal",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 5:17"
    },
    {
        "quote": "The peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
        "emotion": "peace",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:7"
    },
    {
        "quote": "But the one who stands firm to the end will be saved.",
        "emotion": "endurance",
        "author": "Jesus",
        "book": "Matthew",
        "reference": "Matthew 24:13"
    },
    {
        "quote": "When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you.",
        "emotion": "protection",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 43:2"
    },
    {
        "quote": "And God is able to bless you abundantly, so that in all things at all times, having all that you need, you will abound in every good work.",
        "emotion": "abundance",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 9:8"
    },
    {
        "quote": "The Lord is my portion; therefore I will wait for him.",
        "emotion": "hope",
        "author": "Lamentations",
        "book": "Lamentations",
        "reference": "Lamentations 3:24"
    },
    {
        "quote": "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.",
        "emotion": "strength",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 40:31"
    },
    {
        "quote": "The Lord is my strength and my shield; my heart trusts in him, and he helps me.",
        "emotion": "trust",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 28:7"
    },
    {
        "quote": "I will bless the Lord at all times; his praise shall continually be in my mouth.",
        "emotion": "praise",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:1"
    },
     {
        "quote": "The Lord is good to those who hope is in him, to the one who seeks him;",
        "emotion": "goodness",
        "author": "Lamentations",
        "book": "Lamentations",
        "reference": "Lamentations 3:25"
    },
    {
        "quote": "For I am the Lord, the God of all mankind. Is anything too hard for me?",
        "emotion": "omnipotence",
        "author": "God",
        "book": "Jeremiah",
        "reference": "Jeremiah 32:27"
    },
    {
        "quote": "The Lord is my rock, my fortress and my deliverer; my God is my rock, in whom I take refuge.",
        "emotion": "safety",
        "author": "David",
        "book": "2 Samuel",
        "reference": "2 Samuel 22:2"
    },
    {
        "quote": "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
        "emotion": "comfort",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:4"
    },
    {
        "quote": "For the Lord gives wisdom; from his mouth come knowledge and understanding.",
        "emotion": "wisdom",
        "author": "Solomon",
        "book": "Proverbs",
        "reference": "Proverbs 2:6"
    },
    {
        "quote": "The Lord is near to the brokenhearted and saves the crushed in spirit.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:18"
    },
    {
        "quote": "You are the light of the world. A town built on a hill cannot be hidden.",
        "emotion": "light",
        "author": "Jesus",
        "book": "Matthew",
        "reference": "Matthew 5:14"
    },
    {
        "quote": "He who began a good work in you will carry it on to completion until the day of Christ Jesus.",
        "emotion": "assurance",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 1:6"
    },
    {
        "quote": "Be strong and courageous. Do not be afraid or discouraged, for the Lord your God will be with you wherever you go.",
        "emotion": "courage",
        "author": "Joshua",
        "book": "Joshua",
        "reference": "Joshua 1:9"
    },
    {
        "quote": "The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you; the Lord turn his face toward you and give you peace.",
        "emotion": "blessing",
        "author": "Moses",
        "book": "Numbers",
        "reference": "Numbers 6:24-26"
    },
    {
        "quote": "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.",
        "emotion": "trust",
        "author": "Solomon",
        "book": "Proverbs",
        "reference": "Proverbs 3:5-6"
    },
    {
        "quote": "Let all that you do be done in love.",
        "emotion": "love",
        "author": "Paul",
        "book": "1 Corinthians",
        "reference": "1 Corinthians 16:14"
    },
    {
        "quote": "For God did not give us a spirit of timidity, but a spirit of power, of love and of self-discipline.",
        "emotion": "power",
        "author": "Paul",
        "book": "2 Timothy",
        "reference": "2 Timothy 1:7"
    },
    {
        "quote": "This is the day the Lord has made; let us rejoice and be glad in it.",
        "emotion": "joy",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 118:24"
    },
    {
        "quote": "The Lord is righteous in all his ways and faithful in all he does.",
        "emotion": "righteousness",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:17"
    },
    {
        "quote": "You will keep in perfect peace those whose minds are steadfast, because they trust in you.",
        "emotion": "peace",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 26:3"
    },
    {
        "quote": "I will bless the Lord at all times; his praise shall continually be in my mouth.",
        "emotion": "praise",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:1"
    },
    {
        "quote": "I am the way and the truth and the life. No one comes to the Father except through me.",
        "emotion": "truth",
        "author": "Jesus",
        "book": "John",
        "reference": "John 14:6"
    },
    {
        "quote": "For where your treasure is, there your heart will be also.",
        "emotion": "heart",
        "author": "Jesus",
        "book": "Matthew",
        "reference": "Matthew 6:21"
    },
    {
        "quote": "Do not let anyone look down on you because you are young, but set an example for the believers in speech, in conduct, in love, in faith and in purity.",
        "emotion": "example",
        "author": "Paul",
        "book": "1 Timothy",
        "reference": "1 Timothy 4:12"
    },
    {
        "quote": "Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here!",
        "emotion": "renewal",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 5:17"
    },
    {
        "quote": "For we live by faith, not by sight.",
        "emotion": "faith",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 5:7"
    },
    {
        "quote": "The righteous cry out, and the Lord hears them; he delivers them from all their troubles.",
        "emotion": "deliverance",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:17"
    },
    {
        "quote": "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control.",
        "emotion": "fruit of the Spirit",
        "author": "Paul",
        "book": "Galatians",
        "reference": "Galatians 5:22-23"
    },
    {
        "quote": "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.",
        "emotion": "salvation",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 6:23"
    },
    {
        "quote": "For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.",
        "emotion": "love",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:38-39"
    },
    {
        "quote": "The Lord is compassionate and gracious, slow to anger, abounding in love.",
        "emotion": "grace",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 103:8"
    },
    {
        "quote": "I have fought the good fight, I have finished the race, I have kept the faith.",
        "emotion": "endurance",
        "author": "Paul",
        "book": "2 Timothy",
        "reference": "2 Timothy 4:7"
    },
    {
        "quote": "For God has not given us a spirit of fear, but of power, love, and self-discipline.",
        "emotion": "courage",
        "author": "Paul",
        "book": "2 Timothy",
        "reference": "2 Timothy 1:7"
    },
    {
        "quote": "The Lord is my shepherd; I lack nothing.",
        "emotion": "contentment",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:1"
    },
    {
        "quote": "Jesus Christ is the same yesterday and today and forever.",
        "emotion": "constancy",
        "author": "Author of Hebrews",
        "book": "Hebrews",
        "reference": "Hebrews 13:8"
    },
    {
        "quote": "The Lord is close to all who call on him, to all who call on him in truth.",
        "emotion": "nearness",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:18"
    },
    {
        "quote": "For the word of the Lord is right and true; he is faithful in all he does.",
        "emotion": "faithfulness",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 33:4"
    },
    {
        "quote": "Do not be afraid, for I am with you; do not be discouraged, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
        "emotion": "comfort",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 41:10"
    },
    {
        "quote": "The Lord is my light and my salvation— whom shall I fear? The Lord is the stronghold of my life— of whom shall I be afraid?",
        "emotion": "courage",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 27:1"
    },
    {
        "quote": "So do not fear; I will provide for you and your children. And he reassured them and spoke kindly to them.",
        "emotion": "provision",
        "author": "Joseph",
        "book": "Genesis",
        "reference": "Genesis 50:21"
    },
    {
        "quote": "Let all that you do be done in love.",
        "emotion": "love",
        "author": "Paul",
        "book": "1 Corinthians",
        "reference": "1 Corinthians 16:14"
    },
    {
        "quote": "Be joyful in hope, patient in affliction, faithful in prayer.",
        "emotion": "faithfulness",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 12:12"
    },
    {
        "quote": "When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you.",
        "emotion": "protection",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 43:2"
    },
    {
        "quote": "The Lord will fight for you; you need only to be still.",
        "emotion": "peace",
        "author": "Moses",
        "book": "Exodus",
        "reference": "Exodus 14:14"
    },
    {
        "quote": "He heals the brokenhearted and binds up their wounds.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 147:3"
    },
    {
        "quote": "The righteous cry out, and the Lord hears them; he delivers them from all their troubles.",
        "emotion": "deliverance",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:17"
    },
    {
        "quote": "And my God will meet all your needs according to the riches of his glory in Christ Jesus.",
        "emotion": "provision",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:19"
    },
    {
        "quote": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.",
        "emotion": "love",
        "author": "John",
        "book": "John",
        "reference": "John 3:16"
    },{
        "quote": "I can do all this through him who gives me strength.",
        "emotion": "strength",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:13"
    },
    {
        "quote": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
        "emotion": "purpose",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:28"
    },
    {
        "quote": "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.",
        "emotion": "hope",
        "author": "God",
        "book": "Jeremiah",
        "reference": "Jeremiah 29:11"
    },
    {
        "quote": "The Lord is my shepherd, I shall not want.",
        "emotion": "trust",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:1"
    },
    {
        "quote": "He gives strength to the weary and increases the power of the weak.",
        "emotion": "strength",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 40:29"
    },
    {
        "quote": "You will keep in perfect peace those whose minds are steadfast, because they trust in you.",
        "emotion": "peace",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 26:3"
    },
    {
        "quote": "The Lord is my light and my salvation— whom shall I fear? The Lord is the stronghold of my life— of whom shall I be afraid?",
        "emotion": "courage",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 27:1"
    },
    {
        "quote": "I will bless the Lord at all times; his praise shall continually be in my mouth.",
        "emotion": "praise",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:1"
    },
    {
        "quote": "The Lord is my refuge and fortress; my God, in whom I trust.",
        "emotion": "safety",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 91:2"
    },
    {
        "quote": "And we have seen and testify that the Father has sent his Son to be the Savior of the world.",
        "emotion": "testimony",
        "author": "John",
        "book": "1 John",
        "reference": "1 John 4:14"
    },
    {
        "quote": "For the Lord gives wisdom; from his mouth come knowledge and understanding.",
        "emotion": "wisdom",
        "author": "Solomon",
        "book": "Proverbs",
        "reference": "Proverbs 2:6"
    },
    {
        "quote": "Let the peace of Christ rule in your hearts, since as members of one body you were called to peace.",
        "emotion": "peace",
        "author": "Paul",
        "book": "Colossians",
        "reference": "Colossians 3:15"
    },
    {
        "quote": "And God is able to bless you abundantly, so that in all things at all times, having all that you need, you will abound in every good work.",
        "emotion": "provision",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 9:8"
    },
    {
        "quote": "We love because he first loved us.",
        "emotion": "love",
        "author": "John",
        "book": "1 John",
        "reference": "1 John 4:19"
    },
    {
        "quote": "For where your treasure is, there your heart will be also.",
        "emotion": "heart",
        "author": "Jesus",
        "book": "Matthew",
        "reference": "Matthew 6:21"
    },
    {
        "quote": "Cast all your anxiety on him because he cares for you.",
        "emotion": "care",
        "author": "Peter",
        "book": "1 Peter",
        "reference": "1 Peter 5:7"
    },
    {
        "quote": "The Lord is near to the brokenhearted and saves the crushed in spirit.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:18"
    },
    {
        "quote": "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control.",
        "emotion": "fruit of the Spirit",
        "author": "Paul",
        "book": "Galatians",
        "reference": "Galatians 5:22-23"
    },
    {
        "quote": "No one has ever seen God; but if we love one another, God lives in us and his love is made complete in us.",
        "emotion": "love",
        "author": "John",
        "book": "1 John",
        "reference": "1 John 4:12"
    },
    {
        "quote": "But the Lord stood with me and gave me strength, so that through me the message might be fully proclaimed and all the Gentiles might hear it.",
        "emotion": "strength",
        "author": "Paul",
        "book": "2 Timothy",
        "reference": "2 Timothy 4:17"
    },
    {
        "quote": "For God is not the author of confusion but of peace.",
        "emotion": "peace",
        "author": "Paul",
        "book": "1 Corinthians",
        "reference": "1 Corinthians 14:33"
    },{
        "quote": "The Lord is good to all; he has compassion on all he has made.",
        "emotion": "compassion",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:9"
    },
    {
        "quote": "But the Lord stood by me and gave me strength, so that through me the message might be fully proclaimed.",
        "emotion": "strength",
        "author": "Paul",
        "book": "2 Timothy",
        "reference": "2 Timothy 4:17"
    },
    {
        "quote": "The Lord will fight for you; you need only to be still.",
        "emotion": "peace",
        "author": "Moses",
        "book": "Exodus",
        "reference": "Exodus 14:14"
    },
    {
        "quote": "Do not be afraid or discouraged, for the Lord your God will be with you wherever you go.",
        "emotion": "courage",
        "author": "Joshua",
        "book": "Joshua",
        "reference": "Joshua 1:9"
    },
    {
        "quote": "The righteous cry out, and the Lord hears them; he delivers them from all their troubles.",
        "emotion": "deliverance",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:17"
    },
    {
        "quote": "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope.",
        "emotion": "hope",
        "author": "God",
        "book": "Jeremiah",
        "reference": "Jeremiah 29:11"
    },
    {
        "quote": "And God is able to bless you abundantly, so that in all things at all times, having all that you need, you will abound in every good work.",
        "emotion": "provision",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 9:8"
    },
    {
        "quote": "The Lord is my light and my salvation— whom shall I fear? The Lord is the stronghold of my life— of whom shall I be afraid?",
        "emotion": "courage",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 27:1"
    },
    {
        "quote": "Cast all your anxiety on him because he cares for you.",
        "emotion": "care",
        "author": "Peter",
        "book": "1 Peter",
        "reference": "1 Peter 5:7"
    },
    {
        "quote": "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.",
        "emotion": "salvation",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 6:23"
    },
    {
        "quote": "I can do all things through Christ who strengthens me.",
        "emotion": "strength",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:13"
    },
    {
        "quote": "For we walk by faith, not by sight.",
        "emotion": "faith",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 5:7"
    },
    {
        "quote": "The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:18"
    },
    {
        "quote": "The Lord is my shepherd; I shall not want.",
        "emotion": "trust",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:1"
    },
    {
        "quote": "You will keep in perfect peace those whose minds are steadfast because they trust in you.",
        "emotion": "peace",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 26:3"
    },
    {
        "quote": "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control.",
        "emotion": "fruit of the Spirit",
        "author": "Paul",
        "book": "Galatians",
        "reference": "Galatians 5:22-23"
    },
    {
        "quote": "Let everything that has breath praise the Lord.",
        "emotion": "praise",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 150:6"
    },
    {
        "quote": "Be strong and courageous. Do not be afraid or discouraged, for the Lord your God will be with you wherever you go.",
        "emotion": "strength",
        "author": "Joshua",
        "book": "Joshua",
        "reference": "Joshua 1:9"
    },
    {
        "quote": "The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you; the Lord turn his face toward you and give you peace.",
        "emotion": "blessing",
        "author": "Moses",
        "book": "Numbers",
        "reference": "Numbers 6:24-26"
    },
    {
        "quote": "For I am the way and the truth and the life. No one comes to the Father except through me.",
        "emotion": "truth",
        "author": "Jesus",
        "book": "John",
        "reference": "John 14:6"
    },
    {
        "quote": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
        "emotion": "purpose",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:28"
    },{
        "quote": "He who dwells in the secret place of the Most High will rest in the shadow of the Almighty.",
        "emotion": "rest",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 91:1"
    },
    {
        "quote": "The Lord is my refuge and fortress; my God, in whom I trust.",
        "emotion": "safety",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 91:2"
    },
    {
        "quote": "Blessed are the poor in spirit, for theirs is the kingdom of heaven.",
        "emotion": "humility",
        "author": "Jesus",
        "book": "Matthew",
        "reference": "Matthew 5:3"
    },
    {
        "quote": "Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here!",
        "emotion": "newness",
        "author": "Paul",
        "book": "2 Corinthians",
        "reference": "2 Corinthians 5:17"
    },
    {
        "quote": "If God is for us, who can be against us?",
        "emotion": "victory",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:31"
    },
    {
        "quote": "The Lord is near to all who call on him, to all who call on him in truth.",
        "emotion": "nearness",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:18"
    },
    {
        "quote": "God is our refuge and strength, an ever-present help in trouble.",
        "emotion": "strength",
        "author": "Psalmist",
        "book": "Psalms",
        "reference": "Psalm 46:1"
    },
    {
        "quote": "The Lord is gracious and righteous; our God is full of compassion.",
        "emotion": "compassion",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 116:5"
    },
    {
        "quote": "I will not leave you as orphans; I will come to you.",
        "emotion": "comfort",
        "author": "Jesus",
        "book": "John",
        "reference": "John 14:18"
    },
    {
        "quote": "We love because he first loved us.",
        "emotion": "love",
        "author": "John",
        "book": "1 John",
        "reference": "1 John 4:19"
    },
    {
        "quote": "And my God will meet all your needs according to the riches of his glory in Christ Jesus.",
        "emotion": "provision",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:19"
    },
    {
        "quote": "The Lord will fight for you; you need only to be still.",
        "emotion": "peace",
        "author": "Moses",
        "book": "Exodus",
        "reference": "Exodus 14:14"
    },
    {
        "quote": "Do not let your hearts be troubled. You believe in God; believe also in me.",
        "emotion": "faith",
        "author": "Jesus",
        "book": "John",
        "reference": "John 14:1"
    },
    {
        "quote": "The Lord is compassionate and gracious, slow to anger, abounding in love.",
        "emotion": "compassion",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 103:8"
    },
    {
        "quote": "Let everything that has breath praise the Lord.",
        "emotion": "praise",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 150:6"
    },
    {
        "quote": "And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
        "emotion": "peace",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 4:7"
    },
    {
        "quote": "The Lord is my shepherd, I lack nothing.",
        "emotion": "contentment",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:1"
    },
    {
        "quote": "The Lord is my light and my salvation— whom shall I fear? The Lord is the stronghold of my life— of whom shall I be afraid?",
        "emotion": "courage",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 27:1"
    },
    {
        "quote": "He heals the brokenhearted and binds up their wounds.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 147:3"
    },
    {
        "quote": "For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.",
        "emotion": "love",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:38-39"
    },
    {
        "quote": "For the wages of sin is death, but the gift of God is eternal life in Christ Jesus our Lord.",
        "emotion": "salvation",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 6:23"
    },
    {
        "quote": "The Lord is good to all; he has compassion on all he has made.",
        "emotion": "compassion",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 145:9"
    },
    {
        "quote": "Do not be afraid, for I am with you; do not be discouraged, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
        "emotion": "comfort",
        "author": "Isaiah",
        "book": "Isaiah",
        "reference": "Isaiah 41:10"
    },
    {
        "quote": "Let all that you do be done in love.",
        "emotion": "love",
        "author": "Paul",
        "book": "1 Corinthians",
        "reference": "1 Corinthians 16:14"
    },
    {
        "quote": "You are the light of the world. A town built on a hill cannot be hidden.",
        "emotion": "guidance",
        "author": "Jesus",
        "book": "Matthew",
        "reference": "Matthew 5:14"
    },
    {
        "quote": "Be still, and know that I am God.",
        "emotion": "peace",
        "author": "Psalmist",
        "book": "Psalms",
        "reference": "Psalm 46:10"
    },
    {
        "quote": "He who began a good work in you will carry it on to completion until the day of Christ Jesus.",
        "emotion": "encouragement",
        "author": "Paul",
        "book": "Philippians",
        "reference": "Philippians 1:6"
    },
    {
        "quote": "For God has not given us a spirit of fear, but of power, love, and self-discipline.",
        "emotion": "courage",
        "author": "Paul",
        "book": "2 Timothy",
        "reference": "2 Timothy 1:7"
    },
    {
        "quote": "The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
        "emotion": "healing",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 34:18"
    },
    {
        "quote": "The Lord is my shepherd; I shall not want.",
        "emotion": "trust",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 23:1"
    },
    {
        "quote": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose.",
        "emotion": "purpose",
        "author": "Paul",
        "book": "Romans",
        "reference": "Romans 8:28"
    },
    {
        "quote": "For the word of the Lord is right and true; he is faithful in all he does.",
        "emotion": "faithfulness",
        "author": "David",
        "book": "Psalms",
        "reference": "Psalm 33:4"
    },
    {
        "quote": "Do not be afraid or discouraged, for the Lord your God will be with you wherever you go.",
        "emotion": "courage",
        "author": "Joshua",
        "book": "Joshua",
        "reference": "Joshua 1:9"
    },
    {
        "quote": "For I am the way and the truth and the life. No one comes to the Father except through me.",
        "emotion": "truth",
        "author": "Jesus",
        "book": "John",
        "reference": "John 14:6"
    }
]


@app.route("/",methods=["GET"])
def index():
    return """
    <h1>Welcome to the Bible Bot!</h1>
    <p>This is the index page of the Bible Bot.</p>
    <p>If you'd like to access a random verse of the day, please go to <a href="/getbibleverse">/getbibleverse</a>.</p>
    <p>If you'd like to access a verse of the day from a specific author, please go to /author/"author_name".</p>
    <p>If you'd like to access a verse of the day from a specific emotion, please go to /emotion/"emotion_name".</p>
    <p>If you'd like to access a verse of the day from a specific book, please go to /book/"book_name".</p>
    <p>If you'd like to access a verse of the day from a specific author along with a specific emotion, please go to /emotion_author/"author_name"/"emotion_name".</p>
    """

@app.route("/getbibleverse",methods=["GET"])
def bibleverse():
    return random.choice(bible_verse)

@app.route("/author/<string:name>")
def authorverse(name):
    name = name.strip()
    author_verses = [verse for verse in bible_verse if verse["author"].lower() == name.lower()]
    if len(author_verses)==0:
        return {"error":f"No verse for author {name}"}
    else:
        verse = random.choice(author_verses)
        return verse

@app.route("/emotion/<string:emo>")
def emotionverse(emo):
    emotion_verses = [verse for verse in bible_verse if verse["emotion"].lower() == emo.lower()]
    if len(emotion_verses)==0:
        return {"error":f"No verse for emotion {emo}"}
    else:
        return random.choice(emotion_verses)
    
@app.route("/emotion_author/<string:author>/<string:emotion>")
def authoremotionverse(author,emotion):
    author_emotion_verses = [verse for verse in bible_verse if verse["author"].lower() == author.lower() and verse["emotion"].lower()==emotion.lower()]
    if len(author_emotion_verses) == 0:
        return {"error":f"No verse for author {author} with emotion {emotion}"}
    else:
        return random.choice(author_emotion_verses)
    
@app.route("/book/<string:book>")
def bookverse(book):
    bookverses = [verse for verse in bible_verse if verse["book"].lower() == book.lower()]
    if len(bookverses) == 0:
        return {"error":f"No verse for book {book}"}
    else:
        return random.choice(bookverses)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

