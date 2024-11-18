import pygame

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, surface=None, bg_color=None, padx=None, pady=None):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.surface = surface
		self.bg_color = bg_color
		self.padx = padx
		self.pady = pady
		if self.padx is None:
			self.padx = 0
		if self.pady is None:
			self.pady = 0


	def update(self, screen):
		if self.surface is not None and self.bg_color is not None:
			self.draw_rect_alpha()
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	def draw_rect_alpha(self):
		rect = self.text_rect.copy()
		if self.padx is not None:
			rect.width += self.padx
			rect.x -= self.padx / 2
		if self.pady is not None:
			rect.height += self.pady
			rect.y -= self.pady / 2
		shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
		pygame.draw.rect(shape_surf, self.bg_color, shape_surf.get_rect())
		self.surface.blit(shape_surf, rect)