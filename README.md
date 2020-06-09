# DIY-mini-blog

Project developed as an assessment test understanding of how to create a website using Django, as described in the guides provided in [MDN - Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

## Project Brief

<table>
 <thead>
  <tr>
   <th scope="col">Page</th>
   <th scope="col">URL</th>
   <th scope="col">Requirements</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Home page</td>
   <td><code>/</code> and <code>/blog/</code></td>
   <td>An index page describing the site.</td>
  </tr>
  <tr>
   <td>List of all blog posts</td>
   <td><code>/blog/blogs/</code></td>
   <td>
    <p>List of all blog posts:</p>
    <ul>
     <li>Accessible to all users from a sidebar link.</li>
     <li>List sorted by post date (newest to oldest).</li>
     <li>List paginated in groups of 5 articles.</li>
     <li>List items display the blog title, post date, and author.</li>
     <li>Blog post names are linked to blog detail pages.</li>
     <li>Blogger (author names) are linked to blog author detail pages.</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>Blog author (blogger) detail page</td>
   <td><code>/blog/blogger/<em>&lt;author-id&gt;</em></code></td>
   <td>
    <p>Information for a specified author (by id) and list of their blog posts:</p>
    <ul>
     <li>Accessible to all users from author links in blog posts etc.</li>
     <li>Contains some biographical information about the blogger/author.</li>
     <li>List sorted by post date (newest to oldest).</li>
     <li>Not paginated.</li>
     <li>List items display just the blog post name and post date.</li>
     <li>Blog post names are linked to blog detail pages.</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>Blog post detail page</td>
   <td><code>/blog/<em>&lt;blog-id&gt;</em></code></td>
   <td>
    <p>Blog post details.</p>
    <ul>
     <li>Accessible to all users from blog post lists.</li>
     <li>Page contains the blog post: name, author, post date, and content.</li>
     <li>Comments for the blog post should be displayed at bottom.</li>
     <li>Comments should be sorted in order: oldest to most recent.</li>
     <li>Contains link to add comments at end for logged in users (see Comment form page)</li>
     <li>Blog posts and comments need only display plain text. There is no need to support any sort of HTML markup (e.g. links, images, bold/italic, etc).</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>List of all bloggers</td>
   <td><code>/blog/bloggers/</code></td>
   <td>
    <p>List of bloggers on system:</p>
    <ul>
     <li>Accessible to all users from site sidebar</li>
     <li>Blogger names are linked to Blog author detail pages.</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>Comment form page</td>
   <td><code>/blog/<em>&lt;blog-id&gt;</em>/create</code></td>
   <td>
    <p>Create comment for blog post:</p>
    <ul>
     <li>Accessible to logged-in users (only) from link at bottom of blog post detail pages.</li>
     <li>Displays form with description for entering comments (post date and blog is not editable).</li>
     <li>After a comment has been posted, the page will redirect back to the associated blog post page.</li>
     <li>Users cannot edit or delete their posts.</li>
     <li>Logged out users will be directed to the login page to log in, before they can add comments. After logging in, they will be redirected back to the blog page they wanted to comment on.</li>
     <li>Comment pages should include the name/link to the blogpost being commented on.</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>User authentication pages</td>
   <td><code>/accounts/<em>&lt;standard urls&gt;</em></code></td>
   <td>
    <p>Standard Django authentication pages for logging in, out and setting the password:</p>
    <ul>
     <li>Login/out should be accessible via sidebar links.</li>
    </ul>
   </td>
  </tr>
  <tr>
   <td>Admin site</td>
   <td><code>/admin/<em>&lt;standard urls&gt;</em></code></td>
   <td>
    <p>Admin site should be enabled to allow create/edit/delete of blog posts, blog authors and blog comments (this is the mechanism for bloggers to create new blog posts):</p>
    <ul>
     <li>Admin site blog posts records should display the list of associated comments inline (below each blog post).</li>
     <li>Comment names in the Admin site are created by truncating the comment description to 75 characters.</li>
     <li>Other types of records can use basic registration.</li>
    </ul>
   </td>
  </tr>
 </tbody>
</table>

<p>In addition you should write some basic tests to verify:</p>

<ul>
 <li>All model fields have the correct label and length.</li>
 <li>All models have the expected object name (e.g.<code> __str__()</code> returns the expected value).</li>
 <li>Models have the expected URL for individual Blog and Comment records (e.g. <code>get_absolute_url()</code> returns the expected URL).</li>
 <li>The BlogListView (all-blog page) is accessible at the expected location (e.g. /blog/blogs)</li>
 <li>The BlogListView (all-blog page) is accessible at the expected named url (e.g. 'blogs')</li>
 <li>The BlogListView (all-blog page) uses the expected template (e.g. the default)</li>
 <li>The BlogListView paginates records by 5 (at least on the first page)</li>
</ul>

## Testing app on Production

- Visit the heroku [deployment](https://diyblogcb.herokuapp.com/).
- For admin login and testing:
  - Visit login admin at [Admin](https://diyblogcb.herokuapp.com/admin).
  - Admin credentials (username: admin, password: 12345@qwerty)
