import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.set_extent([26, 44, 35, 43])
ax.coastlines()

plt.scatter(df['Longitude'], df['Latitude'], transform=ccrs.Geodetic(),
            color='red', marker='*', s=100)

plt.show()

