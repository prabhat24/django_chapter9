<h3>objective</h3>
1. create django project (rango_project)
2. create django app (rango)
3. create a view to show homepage. (just return some HttpResponse object)
4. In your project urls.py file, add a mapping to the rango apps urls.
5. make urls mapping within the app. ie map app's url to app's view. (/rango/home)
6. Create a new view method called about which returns the following HttpResponse: 
'Rango says here is the about page.'
7. Map this view to `/rango/about/`.For this step,you’ll only need to edit the urls.py
of the Rango app. Remember the `/rango/` part is handled by the projects urls.py.
8. Revise the HttpResponse in the index view to include a link to the about page.
9. In the HttpResponse in the about view include a link back to the main page.
