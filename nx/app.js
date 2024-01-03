function sendMessage() {
    // Lấy giá trị từ ô input
    var userInput = document.getElementById('user-input').value;

    // Kiểm tra xem ô input có dữ liệu không
    if (userInput.trim() === '') {
        return;
    }

    // Hiển thị tin nhắn người dùng
    displayMessage('user', userInput);

    // Gọi API bằng cách sử dụng Fetch API
    fetch('http://localhost:8081/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            // Thêm các header khác từ cURL nếu cần thiết
        },
        body: JSON.stringify({ msg: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Hiển thị tin nhắn từ API
        displayMessage('bot', data.msg);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayMessage(sender, message) {
    // Hiển thị tin nhắn trong phần chat
    var chatMessages = document.getElementById('chat-messages');
    var messageElement = document.createElement('div');
    messageElement.className = sender;
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);

    // Xoay đến cuối phần chat để hiển thị tin nhắn mới nhất
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
