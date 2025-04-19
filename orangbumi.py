import matplotlib.pyplot as plt
import matplotlib.animation as animation

def typing_animation(full_text, interval=150):
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.axis('off')
    text = ax.text(0.5, 0.5, '', ha='center', va='center', fontsize=32, family='monospace')

    def init():
        text.set_text('')
        return text,

    def animate(i):
        text.set_text(full_text[:i])
        return text,

    ani = animation.FuncAnimation(
        fig, animate, frames=len(full_text) + 1,
        init_func=init, interval=interval, blit=True
    )
    return ani

def sliding_animation(full_text, interval=30, slide_width=50):
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_xlim(0, slide_width)
    ax.set_ylim(0, 1)
    ax.axis('off')
    text = ax.text(-len(full_text), 0.5, full_text, ha='left', va='center', fontsize=32, family='monospace')

    def animate(i):
        text.set_position((i - len(full_text), 0.5))
        return text,

    ani = animation.FuncAnimation(
        fig, animate, frames=slide_width + len(full_text),
        interval=interval, blit=True
    )
    return ani

if __name__ == "__main__":
    message = "#savesmansa"
    # To display typing effect:
    ani1 = typing_animation(message, interval=150)
    plt.show()

    # To display sliding effect:
    ani2 = sliding_animation(message, interval=30, slide_width=80)
    plt.show()