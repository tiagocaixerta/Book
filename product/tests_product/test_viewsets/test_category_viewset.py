def test_get_all_category(self):
    response = self.client.get(reverse('category-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    category_data = json.loads(response.content)
    self.assertEqual(category_data["results"][0]["title"], self.category.title)

def test_create_category(self):
    data = json.dumps({"title": "technology"})
    response = self.client.post(
        reverse('category-list'),
        data=data,
        content_type="application/json",
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    created_category = Category.objects.get(title="technology")
    self.assertEqual(created_category.title, "technology")
