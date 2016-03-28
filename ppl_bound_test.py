import EstNumJellyBeans as jelly

estimator = jelly.NumJellyEstimator()

land_frac = .5
ppl = 8e9
pink_frac = .5
estimator.set_land_frac_for_sugar(land_frac)
estimator.set_world_pop(ppl)
estimator.set_frac_ppl_loving_pink(pink_frac)

est = estimator.compute_Njelly_est()

print("\nIt is estimated that when\n", land_frac*100, "percent\nof the land is"+\
      " used for sugar and\n", pink_frac*100, "percent of", int(ppl), \
      "people\nLOVE pink, then there are\n", est, "\nJelly Beans in the world.")