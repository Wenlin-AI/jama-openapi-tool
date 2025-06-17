# Obtaining Jama Client ID and Client Secret

To authenticate with Jama via OAuth you need a **Client ID** and **Client Secret**. The detailed steps for generating these credentials are described in the Jama developer guide at [dev.jamasoftware.com/api](https://dev.jamasoftware.com/api/). Below is a condensed walkthrough.

1. **Open User Profile**
   - Log in to your Jama instance in a web browser.
   - Click your avatar in the top right and choose **Profile**.

2. **Set API Credentials**
   - On the profile page click **Set API Credentials**.
   - Provide a name for your application or integration.
   - Click **Create API Credentials**.

3. **Copy the Client ID and Secret**
   - Jama displays the generated **Client ID** and **Client Secret** once.
   - Record both values immediately. The secret cannot be viewed again later.

4. **Use the Credentials in OAuth**
   - To exchange the credentials for an access token, make a `POST` request to `/rest/oauth/token` on your Jama server.
   - Send `grant_type=client_credentials` in the body and authenticate using HTTP Basic Auth with the Client ID as the username and the Client Secret as the password.
   - The response contains an `access_token` and an `expires_in` duration (usually one hour).

Repeat the token request whenever the access token expires. You can now call Jama REST endpoints by including the access token in the `Authorization: Bearer` header.

For screenshots and more details, consult the full guide at <https://dev.jamasoftware.com/api/>.
