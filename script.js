fetch('points.json')
  .then(res => res.json())
  .then(data => {
    const leaderboard = document.getElementById("leaderboard");
    const users = Object.entries(data.users || {})
      .map(([username, info]) => ({
        username,
        points: info.points || 0,
        social: info.social_media_points || 0
      }))
      .sort((a, b) => (b.points + b.social) - (a.points + a.social));

    users.forEach((user, index) => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <img class="avatar" src="https://github.com/${user.username}.png" alt="${user.username}">
        <h3>#${index + 1} ${user.username}</h3>
        <p>⭐ Points: ${user.points}</p>
        <p>🌐 Social Media: ${user.social}</p>
        <p>🧮 Total: ${user.points + user.social}</p>
      `;

      leaderboard.appendChild(card);
    });
  })
  .catch(err => {
    console.error("Error loading leaderboard:", err);
  });
