
from core.attacks import ATTACKS
from .utils import str2bool, str2float



def set_parser_train(parser):

    parser.add_argument('--log-dir', type=str, default='/')
    parser.add_argument('--data-dir', type=str, default='/')
    parser.add_argument('-d', '--data', type=str, default='cifar10', help='Data to use.')
    parser.add_argument('--augment', type=str, default='base',
                        choices=['none', 'base', 'cutout', 'autoaugment', 'randaugment', 'idbh'],
                        help='Augment training set.')
    parser.add_argument('--take_amount', type=int, default=None, help='Amount of data selected from base dataset.')
    parser.add_argument('--validation', action='store_true', default=False,
                        help='split validation set for early stopping.')
    parser.add_argument('--aux-data-filename', type=str, help='Path to additional Tiny Images data.',
                        default=None)
    parser.add_argument('--aux_take_amount', type=int, default=None,
                        help='Amount of data selected from unlabelled dataset.')
    parser.add_argument('--unsup-fraction', type=float, default=0., help='Ratio of unlabelled data to labelled data.')
    parser.add_argument('--batch-size', type=int, default=128, help='Batch size for training.')
    parser.add_argument('--batch-size-validation', type=int, default=128, help='Batch size for testing.')
    parser.add_argument('-seed', '--seed', type=int, default=1, help='Random seed.')

    parser.add_argument('--desc', type=str, default='none',
                        help='Description of experiment. It will be used to name directories.')
    parser.add_argument('-m', '--model', default='wrn-28-10-swish',
                        help='Model architecture to be used.')
    parser.add_argument('--normalize', type=str2bool, default=True, help='Normalize input.')
    parser.add_argument('-na', '--num-adv-epochs', type=int, default=100, help='Number of adversarial training epochs.')
    parser.add_argument('--adv-eval-freq', type=int, default=10, help='Adversarial evaluation frequency (in epochs).')
    parser.add_argument('--optimizer', default='sgd', help='Type of optimizer.')
    parser.add_argument('--lr', type=float, default=0.1, help='Learning rate for optimizer.')
    parser.add_argument('--weight-decay', type=float, default=5e-4, help='Optimizer (SGD) weight decay.')
    parser.add_argument('--scheduler', default='none', help='Type of scheduler.')
    parser.add_argument('--nesterov', type=str2bool, default=True, help='Use Nesterov momentum.')
    parser.add_argument('--clip-grad', type=float, default=None, help='Gradient norm clipping.')
    parser.add_argument('--resume_path', default='', type=str)
    parser.add_argument('--pre_resume_path', default='', type=str)

    parser.add_argument('-a', '--attack', type=str, choices=ATTACKS, default='linf-pgd', help='Type of attack.')
    parser.add_argument('--attack-eps', type=str2float, default=8 / 255, help='Epsilon for the attack.')
    parser.add_argument('--attack-step', type=str2float, default=2 / 255, help='Step size for PGD attack.')
    parser.add_argument('--attack-iter', type=int, default=10,
                        help='Max. number of iterations (if any) for the attack.')

    parser.add_argument('--debug', action='store_true', default=False,
                        help='Debug code. Run 1 epoch of training and evaluation.')

    parser.add_argument('--beta', default=None, type=float, help='Stability regularization, i.e., 1/lambda in TRADES.')
    parser.add_argument('--ls', type=float, default=0.1, help='label smoothing.')
    parser.add_argument('--AT', type=str, default='standard', help='Adversarial training method.')
    parser.add_argument('--tau', type=float, default=0., help='Weight averaging decay.')

    return parser


def set_parser_eval(parser):

    parser.add_argument('--data-dir', type=str, default='/')
    parser.add_argument('--log-dir', type=str, default='/')
    parser.add_argument('--desc', type=str, help='Description of model to be evaluated.')
    parser.add_argument('--batch-size-validation', type=int, default=128, help='Batch size for testing.')
    parser.add_argument('--seed', type=int, default=1, help='Random seed.')
    parser.add_argument('--save', action='store_true', default=False)

    return parser