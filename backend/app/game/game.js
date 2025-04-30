const allQuestions = [
  {
    "img": "/images/shadows/bear.jpg",
    "question": "What do bears typically eat?",
    "options": {
      "A": "Bamboo",
      "B": "Fish and berries",
      "C": "Insects"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/capra-aegagrus-hircus.jpg",
    "question": "What unique skill do goats have when moving on mountains?",
    "options": {
      "A": "They can climb steep cliffs",
      "B": "They swim fast",
      "C": "They fly short distances"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/cervus-nippon.jpg",
    "question": "What do sika deer use their antlers for?",
    "options": {
      "A": "Flying",
      "B": "Fighting and defense",
      "C": "Hearing"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/crocodilia.jpg",
    "question": "How do crocodiles usually hunt their prey?",
    "options": {
      "A": "They chase prey for miles",
      "B": "They use camouflage and wait",
      "C": "They dig traps"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/cygnus.jpg",
    "question": "Where do swans usually build their nests?",
    "options": {
      "A": "In treetops",
      "B": "On water or near shores",
      "C": "Underground"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/delphinidae.jpg",
    "question": "What are dolphins known for?",
    "options": {
      "A": "Sharp claws",
      "B": "Echolocation skills",
      "C": "Sleeping on land"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/elephantidae.jpg",
    "question": "Why do elephants flap their ears?",
    "options": {
      "A": "To hear better",
      "B": "To cool down",
      "C": "To fly"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/folivora.jpg",
    "question": "Why are sloths so slow?",
    "options": {
      "A": "To save energy",
      "B": "They are lazy",
      "C": "They are always cold"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/fox.jpg",
    "question": "What is the fox known for?",
    "options": {
      "A": "Being clever and agile",
      "B": "Living underwater",
      "C": "Having wings"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/giraffe.jpg",
    "question": "Why do giraffes have long necks?",
    "options": {
      "A": "To reach high leaves",
      "B": "To breathe better",
      "C": "To swim faster"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/gorilla.jpg",
    "question": "Where do gorillas usually spend most of their time?",
    "options": {
      "A": "In trees",
      "B": "In deserts",
      "C": "On the ground"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/hippopotamus-amphibius.jpg",
    "question": "Why do hippos stay in water during the day?",
    "options": {
      "A": "To sleep",
      "B": "To keep cool",
      "C": "To fish"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/kangaroo.jpg",
    "question": "What do kangaroos use their strong tails for?",
    "options": {
      "A": "Balance and support",
      "B": "Fighting",
      "C": "Flying"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/koala.jpg",
    "question": "What do koalas mainly eat?",
    "options": {
      "A": "Bananas",
      "B": "Bamboo",
      "C": "Eucalyptus leaves"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/leopard.jpg",
    "question": "Why are leopards considered good hunters?",
    "options": {
      "A": "They fly silently",
      "B": "They run very fast and climb trees",
      "C": "They swim deep"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/lion.jpg",
    "question": "What role does a lion play in its pride?",
    "options": {
      "A": "Scouting only",
      "B": "Resting all day",
      "C": "Protecting territory and family"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/panda.jpg",
    "question": "What is the panda's main source of food?",
    "options": {
      "A": "Bamboo",
      "B": "Meat",
      "C": "Fish"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/pavo.jpg",
    "question": "Why do peacocks display their feathers?",
    "options": {
      "A": "To attack enemies",
      "B": "To fly faster",
      "C": "To attract mates"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/phocidae.jpg",
    "question": "What is a seal's special skill?",
    "options": {
      "A": "Flying",
      "B": "Climbing trees",
      "C": "Swimming and diving"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/phoenicopteridae.jpg",
    "question": "Why are flamingos pink in color?",
    "options": {
      "A": "Their diet of shrimp",
      "B": "Their feathers are dyed",
      "C": "They bathe in pink water"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/pongo.jpg",
    "question": "What is special about orangutans?",
    "options": {
      "A": "They build nests in trees",
      "B": "They roar loudly",
      "C": "They hunt at night"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/raccoon.jpg",
    "question": "What skill are raccoons best known for?",
    "options": {
      "A": "Using tools",
      "B": "Flying",
      "C": "Running long distances"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/rhinocerotidae.jpg",
    "question": "What material makes up a rhinoceros horn?",
    "options": {
      "A": "Bone",
      "B": "Keratin",
      "C": "Ivory"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/sciuridae.jpg",
    "question": "What do squirrels do in the winter?",
    "options": {
      "A": "Migrate",
      "B": "Sleep in water",
      "C": "Store food and hibernate"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/sphenisciformes.jpg",
    "question": "What is special about penguins?",
    "options": {
      "A": "They can fly",
      "B": "They live in deserts",
      "C": "They swim but don’t fly"
    },
    "answer": "C"
  },
  {
    "img": "/images/shadows/strigiformes.jpg",
    "question": "When do owls usually hunt?",
    "options": {
      "A": "During the day",
      "B": "At night",
      "C": "Only in summer"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/sus-scrofa.jpg",
    "question": "What do wild boars eat?",
    "options": {
      "A": "Only leaves",
      "B": "Everything - they’re omnivores",
      "C": "Only meat"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/tiger.jpg",
    "question": "What makes each tiger unique?",
    "options": {
      "A": "Their stripes are like fingerprints",
      "B": "They lay eggs",
      "C": "They live in the ocean"
    },
    "answer": "A"
  },
  {
    "img": "/images/shadows/wolf.jpg",
    "question": "How do wolves usually communicate?",
    "options": {
      "A": "By blinking",
      "B": "By howling and body language",
      "C": "By dancing"
    },
    "answer": "B"
  },
  {
    "img": "/images/shadows/zebra.jpg",
    "question": "Why do zebras have stripes?",
    "options": {
      "A": "To blend into snow",
      "B": "To confuse predators",
      "C": "To attract insects"
    },
    "answer": "B"
  }
];


function getRandomQuestions(allQuestions, count = 5) {
  const shuffled = [...allQuestions].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, count);
}
  
  let current = 0;
  let score = 0;
  
  function loadQuestion() {
    const q = questions[current];
    document.getElementById("animal-image").src = q.img;
    document.getElementById("question-text").innerText = q.question;
    document.querySelectorAll(".options button")[0].innerText = `A. ${q.options.A}`;
    document.querySelectorAll(".options button")[1].innerText = `B. ${q.options.B}`;
    document.querySelectorAll(".options button")[2].innerText = `C. ${q.options.C}`;
  }
  
  function selectAnswer(option) {
    if (option === questions[current].answer) {
      score++;
    }
    current++;
    if (current < questions.length) {
      loadQuestion();
    } else {
      showResult();
    }
  }
  
  function showResult() {
    document.getElementById("game-area").style.display = "none";
  
    const modal = document.getElementById("result-modal");
    const title = document.getElementById("modal-title");
    const message = document.getElementById("modal-message");
    const statusText = document.getElementById("modal-status");
    const countdownText = document.getElementById("modal-countdown");
    const playAgainBtn = document.getElementById("play-again-btn");

    fetch("/api/game/finish", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: `score=${score}`
    })
    .then(() => fetch("/api/game/status")) 
    .then(res => res.json())
    .then(data => {
      if (score === 5 && !data.has_earned_discount_before && data.plays_today <= 2) {
        title.innerText = "🎉 Congratulations!";
        message.innerText = `You answered ${score}/5 and earned your discount! 🎟️`;
      } else if (data.has_earned_discount_before) {
        title.innerText = "Game Over";
        message.innerText = `You answered ${score}/5. You’ve already earned your one-time discount.`;
      } else if (data.plays_today < 2) {
        title.innerText = "Game Over";
        message.innerText = `You answered ${score}/5. You still have ${2 - data.plays_today} more chance${data.plays_today === 1 ? "" : "s"} today.`;
      } else {
        title.innerText = "Game Over";
        message.innerText = `You answered ${score}/5. You've used all discount attempts today.`;
        startCountdownToMidnight(); 
      }
  
      if (data.has_earned_discount_before) {
        statusText.innerText = "✅ You’ve already earned a discount.";
      } else {
        const remaining = Math.max(0, 2 - data.plays_today);
        statusText.innerText = `🕒 Remaining discount chances today: ${remaining}`;
      }
  
      playAgainBtn.onclick = () => location.reload();
      modal.classList.remove("hidden");
    });
  }  
  
  function goHome() {
    window.location.href = "/home";
  }
  
  window.onload = () => {
    fetch("/api/game/status")
      .then(res => res.json())
      .then(data => {
        document.getElementById("game-area").style.display = "block";
        questions = getRandomQuestions(allQuestions); 
        loadQuestion();

        const remainingText = document.getElementById("remaining-text");
        const countdownText = document.getElementById("countdown-text");
  
        if (data.has_earned_discount_before) {
          remainingText.innerText = "✅ You have already earned a discount.";
        } else if (data.plays_today < 2) {
          remainingText.innerText = `Remaining discount attempts today: ${2 - data.plays_today}`;
        } else {
          remainingText.innerText = "❌ You've used all discount chances today.";
          countdownText.style.display = "block";
          startCountdownToMidnight();
        }
      })
      .catch(err => {
        console.error("Error checking game status:", err);
        alert("Unable to check game status. Please log in again.");
      });
  };  
  
  function startCountdownToMidnight() {
    const countdownElements = [
      document.getElementById("modal-countdown"),
      document.getElementById("countdown-text")
    ];
  
    function updateCountdown() {
      const now = new Date();
      const nextMidnight = new Date();
      nextMidnight.setHours(24, 0, 0, 0);
      const diff = nextMidnight - now;
  
      const hours = String(Math.floor(diff / 1000 / 60 / 60)).padStart(2, '0');
      const minutes = String(Math.floor((diff / 1000 / 60) % 60)).padStart(2, '0');
      const seconds = String(Math.floor((diff / 1000) % 60)).padStart(2, '0');
  
      const text = `⏳ Discount resets in: ${hours}:${minutes}:${seconds}`;
      countdownElements.forEach(el => {
        if (el) el.innerText = text;
      });
    }
  
    updateCountdown();
    setInterval(updateCountdown, 1000);
  }  