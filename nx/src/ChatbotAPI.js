const API = {
  GetChatbotResponse: async (message) => {
    return new Promise(async (resolve, reject) => {
      const apiUrl = process.env.REACT_APP_API_URL;
      try {
        console.log('message:', message);

        if (message === 'hi') {
          resolve('Xin chào, rất vui được nói chuyện với bạn');
        } else {
          console.log('Making API request with message:', message);

          // Thiết lập cấu hình cho fetch
          const requestOptions = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ msg: message }),
          };

          // Sử dụng fetch để gọi API
          const response = await fetch(apiUrl+"/chat", requestOptions);

          // Kiểm tra trạng thái của response
          if (!response.ok) {
            throw new Error('Không thể kết nối đến API');
          }

          // Chuyển đổi response thành dạng JSON
          const responseData = await response.json();

          console.log('API response:', responseData);

          // Lấy dữ liệu từ trường 'Sam' trong response
          const chatbotResponse = responseData.Sam;

          resolve(chatbotResponse);
        }
      } catch (error) {
        console.error('Error making API request:', error);
        reject('Error making API request');
      }
    });
  },
};

export default API;
