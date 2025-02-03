<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://frankdev.ir/images/MC-Status-Discord-Bot.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">MC Status Discord Bot Py</h3>

  <p align="center">
    Source code of the bot to check the number of Minecraft server players in the bot profile
    <br />
  <p align="center">
    سورس کد بات چک کردن تعداد پلیر های سرور ماینکرفتی در پروفایل بات
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://coderhamid.ir/">Creator Site</a>
    &middot;
    <a href="https://discord.com/users/703707009454833715">Report Bug</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project


- English -
Discord bot Python code to detect whether the server is online or offline and to detect the number of players and the specific size of Minecraft server players

- فارسی -
کد پایتون بات دیسکورد برای تشخیص آنلاین بودن سرور یا آفلاین بودن و تشخیص دادن تعداد پلیر ها و اندازه مشخص پلیر های سرور ماینکرفتی


Use the `python status.py` to get started.

برای شروع از `python status.py` استفاده کنید.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

- English -
Codes written in the bot

- فارسی -
کد های نوشته شده در بات

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Bot setup instructions (دستورالعمل های راه اندازی بات)

* pip
  ```sh
  pip install discord
  ```

  * pip
  ```sh
  pip install discord.py
  ```

1.
```python
   TOKEN = 'Your Bot Token'
   ```
2.
```python
   SERVER_IP = 'Your Miencraft Server Ip'
   ```
3. Start Bot (روشن کردن بات)
   ```sh
   python status.py
   ```
   - English -
   Run CMD or Terminal in the file containing the bot code.

   - فارسی -
   سی ام دی یا ترمینال رو در فایلی که کد بات قرار داره ران کنید

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Explanation of the Code (English)

1. **Importing Libraries**: 
   - `discord`: This library is used to interact with the Discord API.
   - `requests`: This library is used to send HTTP requests to APIs.
   - `asyncio`: This library is used for managing asynchronous operations.
   - `commands`: This module helps in creating commands for the Discord bot.

2. **Defining Token and Server IP**: 
   - The bot's token and the IP address of the Minecraft server are defined at the beginning of the code.

3. **Creating the Bot Object**: 
   - An instance of the bot is created using `commands.Bot`, with a command prefix of `!` to trigger commands.

4. **The `update_status` Function**:
   - This function runs in an infinite loop, checking the server status every 10 seconds.
   - If the response is successful (status code 200), it retrieves the number of online players and the maximum players from the JSON response and updates the bot's status to reflect this.
   - If the server is offline or if any error occurs while sending the request, it updates the bot's status to "Server is offline".

5. **The `on_ready` Event**:
   - This event is triggered when the bot successfully connects to Discord. It calls the `update_status` function to start checking the server status.

6. **Running the Bot**: 
   - Finally, the bot is run using the provided token, allowing it to connect to Discord and start functioning.

### Summary of the Approach
- The code uses a loop to continuously check the server status using an external API.
- It handles both online and offline states, ensuring that users are informed about the server's availability.
- The use of asynchronous programming allows the bot to remain responsive while performing periodic checks.

---

### توضیحات کد (فارسی)

1. **وارد کردن کتابخانه‌ها**: 
   - `discord`: این کتابخانه برای تعامل با API دیسکورد استفاده می‌شود.
   - `requests`: این کتابخانه برای ارسال درخواست‌های HTTP به APIها استفاده می‌شود.
   - `asyncio`: این کتابخانه برای مدیریت عملیات غیرهمزمان استفاده می‌شود.
   - `commands`: این ماژول به ایجاد دستورات برای بات دیسکورد کمک می‌کند.

2. **تعریف توکن و IP سرور**: 
   - توکن بات و آدرس IP سرور ماینکرفت در ابتدای کد تعریف می‌شوند.

3. **ایجاد شیء Bot**: 
   - یک نمونه از بات با استفاده از `commands.Bot` ایجاد می‌شود و پیش‌فرض دستورات با `!` تنظیم می‌شود.

4. **تابع `update_status`**:
   - این تابع در یک حلقه بی‌نهایت اجرا می‌شود و هر 10 ثانیه وضعیت سرور را بررسی می‌کند.
   - اگر پاسخ موفقیت‌آمیز باشد (کد وضعیت 200)، تعداد پلیرهای آنلاین و حداکثر پلیرها را از پاسخ JSON دریافت کرده و وضعیت بات را به‌روزرسانی می‌کند.
   - اگر سرور آفلاین باشد یا در هنگام ارسال درخواست خطایی رخ دهد، وضعیت بات به "Server is offline" تغییر می‌یابد.

5. **رویداد `on_ready`**:
   - این رویداد زمانی فعال می‌شود که بات به‌طور موفق به دیسکورد متصل شود. در اینجا تابع `update_status` را فراخوانی می‌کنیم.

6. **اجرای بات**: 
   - در انتها، بات با استفاده از توکن خود اجرا می‌شود تا به دیسکورد متصل شده و شروع به کار کند.

### خلاصه روش
- کد از یک حلقه برای بررسی مداوم وضعیت سرور با استفاده از یک API خارجی استفاده می‌کند.
- هر دو حالت آنلاین و آفلاین را مدیریت می‌کند و اطمینان حاصل می‌کند که کاربران از وضعیت سرور مطلع هستند.
- استفاده از برنامه‌نویسی غیرهمزمان به بات اجازه می‌دهد که در حین انجام بررسی‌های دوره‌ای پاسخگو بماند.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Creators

- English -
The creators of this bot

- فارسی -
سازندگان این بات

### Hamidmine

<a href="https://coderhamid.ir">
  <img src="https://frankdev.ir/images/hamidmine.png" alt="hamidmine image" width="10" height="10" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Hamidmine - [coderhamid.ir](https://coderhamid.ir/) - email@example.com

Project Link: [github.com/hamidmine76b/MC-Status-Bot-Discord-](https://github.com/hamidmine76b/MC-Status-Bot-Discord-)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-url]: https://www.python.org/
