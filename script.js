const leaderboardEl = document.getElementById("leaderboard");

async function fetchLeaderboard() {
  const res = await fetch("https://raw.githubusercontent.com/Abhishek-Sharma182005/CodeQuest-100-Days-DSA/main/points.json");
  const data = await res.json();

  const users = Object.entries(data.users || {}).map(([username, info]) => ({
    username,
    questPoints: info.points || 0,
    socialPoints: info.social_media_points || 0,
    totalPoints: (info.points || 0) + (info.social_media_points || 0),
  }));

  const sortedUsers = users.sort((a, b) => b.totalPoints - a.totalPoints);

  sortedUsers.forEach((user, index) => {
    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <img class="avatar" src="https://github.com/${user.username}.png" alt="${user.username}">
      <div class="username">@${user.username}</div>
      <div class="stats">
        <div class="stat">
          <div class="stat-value">${user.questPoints}</div>
          <div class="stat-label">Quest</div>
        </div>
        <div class="stat">
          <div class="stat-value">${user.socialPoints}</div>
          <div class="stat-label">Influence</div>
        </div>
        <div class="stat">
          <div class="stat-value">${user.totalPoints}</div>
          <div class="stat-label">Total</div>
        </div>
      </div>
      <div class="rank">🌟 Rank #${index + 1}</div>
    `;

    leaderboardEl.appendChild(card);
  });
}

fetchLeaderboard();

// Activate Vanta.js background
VANTA.GLOBE({
  el: "#vanta-bg",
  mouseControls: true,
  touchControls: true,
  minHeight: 200.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
  size: 1.2,
  backgroundColor: 0x000000,
  color: 0x7700ff
});
