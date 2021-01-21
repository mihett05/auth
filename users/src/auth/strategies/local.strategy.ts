import { Injectable, UnauthorizedException } from '@nestjs/common';

import { Strategy } from 'passport-local';
import { PassportStrategy } from '@nestjs/passport';
import { AuthService } from '../auth.service';
import { User } from '../../users/entities/user.entity';


@Injectable()
export class LocalStrategy extends PassportStrategy(Strategy) {
  constructor(private readonly _authService: AuthService) {
    super({
      'usernameField': 'username'
    });
  }

  async validate(username: string, password: string): Promise<User> {
    const user = await this._authService.validate(username, password);
    if (!user) {
      throw new UnauthorizedException();
    }
    return user;
  }
}